if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
import pandas as pd


def lowercase_column_names(df):
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_')
    return df


def clean_data(df):
    df_cleaned = df
    # drop 'CONTRIBUTING_FACTOR_1', 'CONTRIBUTING_FACTOR_2' columns due 98% percent of missing values
    df_cleaned['CRASH DATETIME'] = pd.to_datetime(df_cleaned['CRASH_DATE'] + ' ' + df_cleaned['CRASH_TIME'])
    df_cleaned = df.drop(['CRASH_DATE', 'CRASH_TIME', 'CONTRIBUTING_FACTOR_1', 'CONTRIBUTING_FACTOR_2'], axis=1)

    # replace missing and invalid value in age with mean value
    age_for_missing_and_invalid_values = df_cleaned[df_cleaned['PERSON_AGE'] > 0]['PERSON_AGE'].mean()
    age_for_missing_and_invalid_values = int(round(age_for_missing_and_invalid_values))
    df_cleaned['PERSON_AGE'].fillna(age_for_missing_and_invalid_values, inplace=True)
    df_cleaned.loc[df['PERSON_AGE'] <= 0, 'PERSON_AGE'] = age_for_missing_and_invalid_values
    
    # replace null values in person sex
    df_cleaned['PERSON_SEX'].fillna('U', inplace=True)
    return df_cleaned



@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
  
    data = clean_data(data)

    data = lowercase_column_names(data)
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
