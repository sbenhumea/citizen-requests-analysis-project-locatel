"""
Shared utils of the project. Used in notebooks 01 to 05. Responsible for file paths, data load, splits and metrics.
"""
from pathlib import Path
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT_DIR / 'data' / 'raw'
PROCESSED_DIR = ROOT_DIR / 'data' / 'processed'
MODELS_DIR = ROOT_DIR / 'models'
FIGURES_DIR = ROOT_DIR / 'docs' / 'figures'
DATASET_MODEL_PATH = PROCESSED_DIR / 'dataset_model.parquet'

def load_model_data(path=DATASET_MODEL_PATH):
    """
    Loads the modeling dataset and returns a dataframe.
    """
    return pd.read_parquet(path)

# TODO: Define temporal split and evaluation metrics 