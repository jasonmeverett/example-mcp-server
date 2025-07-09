# main.py
from server import mcp
import os 

# Import tools so they get registered via decorators
import tools.csv_reader
import tools.calculator


def main():
    transport = os.getenv("MCP_TRANSPORT", "stdio")
    print(f"Starting Iceberg MCP Server via transport: {transport}")
    mcp.serve(transport=transport)


if __name__ == "__main__":
    main()
