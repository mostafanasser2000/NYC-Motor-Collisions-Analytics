import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://data.cityofnewyork.us/api/views/f55k-p6yu/rows.csv?accessType=DOWNLOAD&api_foundry=true'
    persons_dtypes = {
                    'UNIQUE_ID': pd.Int64Dtype(),
                    'COLLISION_ID':pd.Int64Dtype(),
                    'PERSON_ID': str,
                    'PERSON_TYPE': str,
                    'PERSON_INJURY': str,
                    'VEHICLE_ID': str,
                    'PERSON_AGE': pd.Int64Dtype(),
                    'EMOTIONAL_STATUS': str,
                    'BODILY_INJURY': str,
                    'POSITION_IN_VEHICLE': str,
                    'SAFETY_EQUIPMENT': str,
                    'CONTRIBUTING_FACTOR_1': str,
                    'CONTRIBUTING_FACTOR_2': str,
                    'PERSON_SEX': str
                }
    choosing_columns = list(persons_dtypes.keys()) + ['CRASH_DATE', 'CRASH_TIME']
    return pd.read_csv(url, usecols=choosing_columns, dtype=persons_dtypes)

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
