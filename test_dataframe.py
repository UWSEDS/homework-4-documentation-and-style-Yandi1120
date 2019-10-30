'''
The module reads in a url and creates a dataframe,
and returns True if the dataframe satisfies the following:
1. Contains only the columns that are specified
2. Values in each column have the same python type
3. Has at least 10 rows
Also, there are 3 tests that check if all columns have values of the corect type;
if there are nan values; if the dataframe has at least one row.
'''

# Question 1
# Replicate what was done in item (2) for HW2.

import pytest
import pandas as pd
import numpy as np


def read_url_and_create_csv(url_to_read):
    '''read a csv from  url and create corresponding dataframe'''
    dat = pd.read_csv(url_to_read)
    return dat


def same_type(data_list):
    '''returns True if all elements have same type as first one'''
    is_same_type = True
    first_item = data_list[0]
    for item in data_list[1:]:
        if type(first_item) == type(item) or np.isnan(item):
            pass
        else:
            is_same_type = False
    return is_same_type


def tes_create_dataframe(pd_df, col_list):
    '''test if the following conditions are satisfied:
       1. pd_df contains only the columns specified in col_list.
       2. Values in each column have the same python type.
       3. There are at least 10 rows in pd_df
    '''
    result = True
    df_col_list = pd_df.columns.tolist()
    if pd_df[df_col_list[0]].count() + 1 >= 10:
        for df_col in df_col_list:
            if df_col in col_list:
                if same_type(pd_df[df_col].tolist()):
                    pass
                else:
                    result = False
            else:
                result = False
        for col in col_list:
            if col in df_col_list:
                pass
            else:
                result = False
    else:
        result = False
    return result


# Question 2

# Import pronto.csv as our test dataset
DAT = read_url_and_create_csv(
    "https://data.seattle.gov/api/views/tw7j-dfaw/rows.csv?accessType=DOWNLOAD")

# Create lists of column names for testing
LST0 = DAT.columns.tolist() # full list
LST1 = ["bikeid"] # list with only 1 column name
LST2 = ["trip_id", "tripduration", "from_station_id", "age", "bikecolor"]
# column containing new column names
LST3 = ["bikeid", "from_station_name", "to_station_name", "usertype", "birthyear"]
# column not containing new column names
LST4 = DAT.columns.tolist() + ["age", "bikecolor"]

# Check that all columns have values of the correct type.
# Since all items in column "bikeid" are strings, we expect the result to be True.


def test_type():
    '''Test if all columns have values of the correst type'''
    result = tes_create_dataframe(DAT[LST1], LST1)
    assert result

# Check for nan values.
# Let's first create a dataframe that contains nan values.
SUBDAT = DAT[LST3]
SUBDAT = SUBDAT.append(
    {"bikeid": 'SEA01120', "birthyear": 1992}, ignore_index=True)
# We expect the result to be True.


def test_nan():
    '''test that function does not break when we have nan values'''
    result = tes_create_dataframe(SUBDAT, LST3)
    assert result

# Verify that the dataframe has at least one row.
# Since there are 275091 rows, we expect the result to be True.


def test_at_least_one_row():
    '''test that the dataframe has at least one row'''
    result = tes_create_dataframe(DAT, LST0)
    assert result
