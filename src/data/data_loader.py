from dataclasses import dataclass

import pandas as pd


@dataclass
class DataSchema:
    AMOUNT = "amount"
    CATEGORY = "category"
    DATE = "date"
    DESCRIPTION = "description"
    MONTH = "month"
    YEAR = "year"


def load_transactions(path: str) -> pd.DataFrame:
    df = pd.read_csv(
        path,
        dtype={
            DataSchema.AMOUNT: "float",
            DataSchema.DESCRIPTION: "str",
            DataSchema.CATEGORY: "str",
        },
        parse_dates=[DataSchema.DATE],
    )
    df[DataSchema.MONTH] = df[DataSchema.DATE].dt.month.astype(str)
    df[DataSchema.YEAR] = df[DataSchema.DATE].dt.year.astype(str)
    df[DataSchema.AMOUNT] = (
        df[DataSchema.AMOUNT].replace("',", "").astype("float")
    )
    return df
