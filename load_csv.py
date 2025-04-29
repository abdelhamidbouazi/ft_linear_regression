import pandas as pd
from pandas import DataFrame


def load(path: str) -> DataFrame:
    """the main load function
    Args:
        path (str): path to the file
    Returns:
        DataFrame: the data loaded from csv file
    """
    try:
        df = pd.read_csv(path)
        # print(f"Loading dataset of dimensions {df}")
        return df
    except (FileNotFoundError, pd.errors.EmptyDataError,
            pd.errors.ParserError, KeyError) as e:
        raise f"Error: {e}"
