"""
Command-line interface for the Octagon VC Agents.

This module provides a command-line interface for running and installing the MCP server.
"""

import getpass
import json
import os
import platform
import sys
from pathlib import Path
from typing import Dict, List, Optional

import typer
from openai import OpenAI
from rich.console import Console

from .server import mcp  # Import the MCP server instance directly
from .client import octagon_client  # Import the Octagon client instance

app = typer.Typer(help="Octagon VC Agents - AI-driven venture capitalist agents powered by Octagon Private Markets")
console = Console()


def which(cmd: str, path: Optional[str] = None) -> Optional[str]:
    """Find the path to an executable."""
    if path is None:
        path = os.environ.get("PATH", "")

    if platform.system() == "Windows":
        cmd = cmd + ".exe"
        paths = path.split(";")
    else:
        paths = path.split(":")

    for p in paths:
        cmd_path = os.path.join(p, cmd)
        if os.path.isfile(cmd_path) and os.access(cmd_path, os.X_OK):
            return cmd_path

    return None


def update_claude_config(
    server_name: str, command: str, args: List[str], env_vars: Optional[Dict[str, str]] = None
) -> bool:
    """Update the Claude desktop app configuration to include this server."""
    # Find the Claude config file
    config_file = None
    if platform.system() == "Darwin":  # macOS
        config_file = Path(
            Path.home(), "Library", "Application Support", "Claude", "servers_config.json"
        )
    elif platform.system() == "Windows":
        config_file = Path(Path.home(), "AppData", "Roaming", "Claude", "servers_config.json")
    elif platform.system() == "Linux":
        config_file = Path(Path.home(), ".config", "Claude", "servers_config.json")

    if not config_file:
        console.print("[bold red]Error:[/] Could not determine Claude config file location.")
        return False

    # Create the config file if it doesn't exist
    config_file.parent.mkdir(parents=True, exist_ok=True)
    if not config_file.exists():
        config_file.write_text("{}")

    try:
        config = json.loads(config_file.read_text())
        if "mcpServers" not in config:
            config["mcpServers"] = {}

        # Always preserve existing env vars and merge with new ones
        if server_name in config["mcpServers"] and "env" in config["mcpServers"][server_name]:
            existing_env = config["mcpServers"][server_name]["env"]
            if env_vars:
                # New vars take precedence over existing ones
                env_vars = {**existing_env, **env_vars}
            else:
                env_vars = existing_env

        server_config = {"command": command, "args": args}

        # Add environment variables if specified
        if env_vars:
            server_config["env"] = env_vars

        config["mcpServers"][server_name] = server_config

        config_file.write_text(json.dumps(config, indent=2))
        console.print(f"[bold green]Success:[/] Added server '{server_name}' to Claude config")
        return True
    except Exception as e:
        console.print(f"[bold red]Error:[/] Failed to update Claude config: {str(e)}")
        return False


@app.command()
def run() -> None:
    """Run the Octagon Investor Agents Tool MCP server."""
    mcp.run()


@app.command()
def install() -> None:
    """Install the server in the Claude desktop app."""
    name = "octagon-vc-agents"

    env_dict = {}
    local_bin = Path(Path.home(), ".local", "bin")
    pyenv_shims = Path(Path.home(), ".pyenv", "shims")
    path = os.environ["PATH"]
    python_version = platform.python_version()
    python_bin = Path(Path.home(), "Library", "Python", python_version, "bin")

    if platform.system() == "Windows":
        env_dict["PATH"] = f"{local_bin};{pyenv_shims};{python_bin};{path}"
    else:
        env_dict["PATH"] = f"{local_bin}:{pyenv_shims}:{python_bin}:{path}"

    api_key = os.environ.get("OPENAI_API_KEY", "")
    while not api_key:
        api_key = getpass.getpass("Enter your OpenAI API key: ")
        if api_key:
            client = OpenAI(api_key=api_key)
            try:
                client.models.list()
            except Exception as e:
                console.print(
                    f"[bold red]Error:[/] Failed to authenticate with OpenAI API: {str(e)}"
                )
                api_key = ""

    env_dict["OPENAI_API_KEY"] = api_key

    # Add Octagon API key
    octagon_api_key = os.environ.get("OCTAGON_API_KEY", "")
    while not octagon_api_key:
        octagon_api_key = getpass.getpass("Enter your Octagon API key: ")
    env_dict["OCTAGON_API_KEY"] = octagon_api_key

    uv = which("uvx", path=env_dict["PATH"])
    command = uv if uv else "uvx"
    args = [name]

    if update_claude_config(name, command, args, env_vars=env_dict):
        console.print(f"[bold green]Success:[/] Successfully installed {name} in Claude app")
    else:
        console.print(f"[bold red]Error:[/] Failed to install {name} in Claude app")
        sys.exit(1)


def main():
    """Entry point for the CLI when installed via pip/pipx."""
    app()


if __name__ == "__main__":
    main()
