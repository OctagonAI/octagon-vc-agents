"""
Octagon client configuration and initialization.
"""

import os
import sys
from openai import AsyncOpenAI
from rich.console import Console

console = Console()

def get_octagon_client() -> AsyncOpenAI:
    """Initialize and return Octagon client with current environment variables"""
    api_key = os.environ.get("OCTAGON_API_KEY")
    if not api_key:
        console.print("[bold red]Error:[/] OCTAGON_API_KEY environment variable is not set")
        console.print("Please set it using: export OCTAGON_API_KEY=your_api_key")
        sys.exit(1)
    
    return AsyncOpenAI(
        api_key=api_key,
        base_url=os.environ.get("OCTAGON_BASE_URL", "https://api-gateway.octagonagents.com/v1")
    )

octagon_client = get_octagon_client() 