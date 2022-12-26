import pandas as pd
import pdb


def log_print(value):
    print('------------------------------------------',value,'------------------------------------------', sep='\n')


person_df: pd.DataFrame = pd.read_csv('personData.csv')
# log_print(f'person_df takes up {sys.getsizeof(person_df)} bytes')
# pdb.runeval("log_print(f'person_df takes up {sys.getsizeof(person_df)} bytes')")
user_df: pd.DataFrame = pd.read_csv('userData.csv')
# log_print(f'user_df takes up {sys.getsizeof(user_df)} bytes')
# pdb.runeval("log_print(f'user_df takes up {sys.getsizeof(user_df)} bytes')")

#using an innerjoin to only grab rows that have the email field
combined_df: pd.DataFrame = pd.merge(person_df, user_df, left_on='email', right_on='email')
#no idea how to decide how to choose which is correct, in the future would try to use creation date to decide which is the most up to date version of entry
pdb.runeval('print(combined_df.head())')
nan_rows: pd.DataFrame = combined_df.loc[combined_df.isna().any(axis=1)]
pdb.runeval('print(nan_rows.head())')
full_rows: pd.DataFrame = combined_df.dropna(how='any', axis=0)

#no idea how to decide how to choose which is correct, in the future would try to use creation date to decide which is the most up to date version of entry
full_rows.drop_duplicates(subset='email', inplace=True)
pdb.runeval('print(full_rows.head())')
full_rows.sort_values(by='email', inplace=True)
pdb.runeval('print(full_rows.head())')
