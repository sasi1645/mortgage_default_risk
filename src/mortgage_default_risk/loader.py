import pandas as pd
from mortgage_default_risk.features import COLUMNS
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = PROJECT_ROOT/ "data"/ "raw"
PROCESSED_DIR = PROJECT_ROOT/ "data"/ "processed"

def find_file(quarter:str)->Path:
    file_match = RAW_DIR/f"{quarter}.csv"
    if not file_match.exists():
        raise FileNotFoundError(f"No file {quarter} was found in {RAW_DIR}.")
    return file_match

def read_sample(quarter:str,rows:int)->pd.DataFrame:
    file = find_file(quarter)
    df = pd.read_csv(file,header=None,sep="|",names=COLUMNS,dtype=str,nrows=rows)
    return df

def count_non_empty_values(quarter:str,chunksize:int):
    file = find_file(quarter)
    total_non_empty = 0
    total_rows = 0
    reader = pd.read_csv(file,header=None,sep="|",names = COLUMNS,dtype=str,chunksize=chunksize)
    for chunk in reader:
        non_empty_per_chunk = chunk.notna().sum()
        total_non_empty += non_empty_per_chunk
        total_rows += len(chunk)
    return total_non_empty,total_rows
   