# read csv with pandas

import pandas as pd

from utils import remove_date_1


# student incomes
# regular incomes


def convert_to_float(df: pd.DataFrame):
    if 'В час' in df.columns:
        df['В час'] = df['В час'].astype(float)
    return df


def calculate_totals(df: pd.DataFrame, file_name: str) -> None:
    """
    Кароче алгоритм такой:
    1. Считаем сколько часов в неделю есть уроков с учениками (просто суммируем колонку Кол-во часов в неделю)
    2. Считаем сколько часов в месяц есть уроков с учениками (просто суммируем колонку Кол-во часов в неделю * 4)
    ...
    """
    df['В неделю'] = df['Кол-во часов в неделю'] * df['В час']
    df['В месяц'] = df['Кол-во часов в неделю'] * 4 * df['В час']
    df['В год'] = df['В месяц'] * 12
    df.to_csv(f'{file_name}.csv', index=False)


def read_df_by_name(name: str) -> pd.DataFrame:
    return pd.read_csv(f'{name}.csv')


def main():
    for name in ['regular_incomes', 'student_incomes']:
        df = read_df_by_name(name)
        df = remove_date_1(df)
        df = convert_to_float(df)
        calculate_totals(df, name)

    from process_expenses import expenses_run
    expenses_run()


main()
