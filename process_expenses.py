import pandas as pd

from utils import remove_date_1


def convert_to_float_from_gbp(df: pd.DataFrame):
    if 'В месяц' in df.columns:
        df['В месяц'] = df['В месяц'].str.replace('£', '').astype(float)
    return df


def calculate_total_expenses(df: pd.DataFrame) -> None:
    df['В неделю'] = round(df['В месяц'] / 4, 1)
    df['В год'] = round(df['В месяц'] * 12, 1)
    df['В день'] = round(df['В месяц'] / 30, 1)
    df.to_csv('expenses.csv', index=False)


# create function which will drop columns

def expenses_run():
    data_frame = pd.read_csv('expenses.csv')
    data_frame = remove_date_1(data_frame)
    data_frame = convert_to_float_from_gbp(data_frame)
    calculate_total_expenses(data_frame)
