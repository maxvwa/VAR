import pandas as pd
import numpy as np


class VAR:
    
    @staticmethod
    def get_lags(df: pd.DataFrame, lag_order: int, trim: int = 0) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Returns Tuple of DataFrames with Z matrix and Y matrix."""
        n_regressands = df.shape[1]
        data = df.copy()
        cols = data.columns
        for p in range(lag_order):
            for col in cols:
                data[f'{col}_lag_{p + 1}'] = data[col].shift(p + 1)

        if trim != 0:
            lag_order = trim - 1

        return data.iloc[lag_order + 1:, n_regressands:].T, data.iloc[lag_order + 1:, :n_regressands].T
