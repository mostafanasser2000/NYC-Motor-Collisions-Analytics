import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

def lowercase_column_names(df):
    df.columns = df.columns.str.lower()
    df.columns = df.columns.str.replace(' ', '_')
    return df


def clean_data(df):
    df_cleaned = df
    # combine crash date and crash time into one field
    df_cleaned['CRASH DATETIME'] = pd.to_datetime(df_cleaned['CRASH DATE'] + ' ' + df_cleaned['CRASH TIME'])
    df_cleaned.drop(['CRASH DATE', 'CRASH TIME'], axis=1, inplace=True)

    # handle missing values in 
    df_cleaned.fillna({'CONTRIBUTING FACTOR VEHICLE 1': 'Unspecified', 
           'CONTRIBUTING FACTOR VEHICLE 2': 'Unspecified',
           'CONTRIBUTING FACTOR VEHICLE 3': 'Unspecified',
           'CONTRIBUTING FACTOR VEHICLE 4': 'Unspecified',
           'CONTRIBUTING FACTOR VEHICLE 5': 'Unspecified'}, inplace=True)

    df_cleaned['CONTRIBUTING FACTOR VEHICLE 1'] = df_cleaned['CONTRIBUTING FACTOR VEHICLE 1'].apply(lambda x: 'Unspecified' if x.isdigit() else x)
    df_cleaned['CONTRIBUTING FACTOR VEHICLE 2'] = df_cleaned['CONTRIBUTING FACTOR VEHICLE 2'].apply(lambda x: 'Unspecified' if x.isdigit() else x)
    df_cleaned['CONTRIBUTING FACTOR VEHICLE 3'] = df_cleaned['CONTRIBUTING FACTOR VEHICLE 3'].apply(lambda x: 'Unspecified' if x.isdigit() else x)
    df_cleaned['CONTRIBUTING FACTOR VEHICLE 4'] = df_cleaned['CONTRIBUTING FACTOR VEHICLE 4'].apply(lambda x: 'Unspecified' if x.isdigit() else x)
    df_cleaned['CONTRIBUTING FACTOR VEHICLE 5'] = df_cleaned['CONTRIBUTING FACTOR VEHICLE 5'].apply(lambda x: 'Unspecified' if x.isdigit() else x)
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
