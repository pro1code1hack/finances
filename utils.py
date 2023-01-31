def remove_date_1(df):
    if 'Date 1' in df.columns:
        df = df.drop(['Date 1'], axis=1)
    return df
