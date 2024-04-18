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

    url = 'https://data.cityofnewyork.us/api/views/h9gi-nx95/rows.csv'
    crashes_dtypes = {
                    'COLLISION_ID': pd.Int64Dtype(),
                    'BOROUGH':str,
                    'ZIP CODE': str,
                    'ON STREET NAME': str,
                    'NUMBER OF PERSONS INJURED': pd.Int64Dtype(),
                    'NUMBER OF PERSONS KILLED': pd.Int64Dtype(),
                    'NUMBER OF PEDESTRIANS INJURED': pd.Int64Dtype(),
                    'NUMBER OF PEDESTRIANS KILLED': pd.Int64Dtype(),
                    'NUMBER OF CYCLIST INJURED': pd.Int64Dtype(),
                    'NUMBER OF CYCLIST KILLED': pd.Int64Dtype(),
                    'NUMBER OF MOTORIST INJURED': pd.Int64Dtype(),
                    'NUMBER OF MOTORIST KILLED': pd.Int64Dtype(),
                    'CONTRIBUTING FACTOR VEHICLE 1': str,
                    'CONTRIBUTING FACTOR VEHICLE 2': str,
                    'CONTRIBUTING FACTOR VEHICLE 3': str,
                    'CONTRIBUTING FACTOR VEHICLE 4': str,
                    'CONTRIBUTING FACTOR VEHICLE 5': str,
                    'VEHICLE TYPE CODE 1': str,
                    'VEHICLE TYPE CODE 2': str,
                    'VEHICLE TYPE CODE 3': str,
                    'VEHICLE TYPE CODE 4': str,
                    'VEHICLE TYPE CODE 5': str,

                }
    choosing_columns = list(crashes_dtypes.keys()) + ['CRASH DATE', 'CRASH TIME']
    return pd.read_csv(url, usecols=choosing_columns, dtype=crashes_dtypes)
  
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
