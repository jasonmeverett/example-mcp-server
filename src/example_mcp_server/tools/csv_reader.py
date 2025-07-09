# utils/file_reader.py

from server import mcp
import pandas as pd
from pathlib import Path

# Base directory where our data lives.
# this file is src/example_mcp_server/tools/csv_reader.py
# so the data directory is data/
DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"

@mcp.tool()
def read_csv(filename: str) -> str:
    """
    Read a static CSV dataset file from a the data directory.
    Args:
        filename: Name of the CSV file (e.g. 'sample.csv')
    Returns:
        A string describing the file's contents.
    """
    file_path = DATA_DIR / filename
    df = pd.read_csv(file_path)
    return df.to_string()
