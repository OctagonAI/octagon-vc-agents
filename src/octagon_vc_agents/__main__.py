"""
Main entry point for the Octagon octagon-vc-agents.

This module provides the main entry point for running the MCP server.
"""

import os
import sys

from octagon_vc_agents.server import mcp


def main() -> None:
    """Run the MCP server."""
    # Check if the OpenAI API key is set
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable is not set.")
        print("Please set it before running the server.")
        sys.exit(1)

    # Check if the Octagon API key is set
    if not os.environ.get("OCTAGON_API_KEY"):
        print("Error: OCTAGON_API_KEY environment variable is not set.")
        print("Obtain your API key at https://app.octagonai.co/signup")
        print("Please set it before running the server.")
        sys.exit(1)
    
    # Get the transport from environment variables or use default
    transport = os.environ.get("MCP_TRANSPORT", "stdio")

    print(f"Starting OpenAI Agents MCP server with {transport} transport")

    # Run the server using the FastMCP's run method
    mcp.run(transport=transport)


if __name__ == "__main__":
    main()