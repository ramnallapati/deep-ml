# Cell 1
import pandas as pd

def first_look(df):
    """Return (shape, summary) where summary has one row per column of df."""

    shape = df.shape

    summary = pd.DataFrame({
        'column': df.columns,
        'dtype': df.dtypes.astype(str).values,
        'missing': df.isnull().sum().values,
        'unique': df.nunique().values
    })

    return shape, summary