#!/usr/bin/env python

#####################################################
# File name: pre_processing.py                      #
# Author: Parth Mehta, Vidya Venkiteswaran          #
# Email: pm2877@columbia.edu, vv2269@columbia.edu   #
# Date created: 02/26/2017                          #
# Usage: python pre_processing.py                   #
# Python Version: 3.4, 3.5, 3.6                     #
# Instructor: Prof. Andreas Mueller                 #
#####################################################
import math

def collapse_columns(housing_data):
    """Collapse Columns into one

    Give out a score for house feature like stairways, floors, walls,
    and windows and add it to pandas data frame. Plus remove these columns
    from pandas dataframe. 

    Initially all the houses have score 0
    1. Value 1 corresponds to the fact that nothing was wrong with the house.
       So, we add +(val) where val is the number of things that could have
       been wrong with the house corresponding to that feature
    2. Value of 9 corresponds to the fact that something was wrong with the 
       house and needs to be subtracted form the score.
    3. Value of 8 suggests that there wasn't any response, hence nothing needs
       be subtracted/added to the score

    Parameters
    ----------
    housing_data : pandas
                   housing data from csv

    Returns
    -------
    housing_data : pandas
        preprocessed data
    """

    # Store features pertaining to house
    walls = ['uf1_1', 'uf1_2', 'uf1_3','uf1_4']
    windows = ['uf1_7', 'uf1_8', 'uf1_9']
    stairways = ['uf1_12', 'uf1_13']
    floors = ['uf1_17', 'uf1_18','uf1_19','uf1_20']

    scores = []
    for index, row in housing_data.iterrows():
        score = 0
        if row['uf1_5'] == 1:
            score += 4
        elif row['uf1_5'] == 9:
            score -= sum(1 for wall in walls if row[wall] ==  1)

        if row['uf1_10'] == 1:
            score += 4
        elif row['uf1_10'] == 9:
            score -= sum(1 for window in windows if row[window] ==  1)

        if row['uf1_14'] == 1:
            score += 2
        elif row['uf1_14'] == 9:
            if row['uf1_15'] == 1:
                score += 1
            if row['uf1_16'] == 1:
                score += 1
            if row['uf1_15'] != 1 and row['uf1_16'] != 1:
                score -= sum(1 for stairway in stairways if row[stairway] ==  1)

        if row['uf1_21'] == 1:
            score += 4
        elif row['uf1_21'] == 9:
            score -= sum(1 for floor in floors if row[floor] ==  1) 

        # to keep the score positive
        scores.append(score+14)
    # add it to the pandas dataframe
    housing_data['score'] = scores 

    # drop columns which have been used to generate score for the house
    col_drop = ['uf1_'+str(col) for col in range(1,23)]
    col_drop.append('uf1_35')
    housing_data = housing_data.drop(col_drop, axis=1)

    return housing_data


def remove_empty(X):
    """Preprocess data

    Remove from the target column (uf17) non applicable
    data like 99999 and 7999

    Parameters
    ----------
    X : pandas
        original data (unprocessed)

    Returns
    -------
    X : pandas
        removed target values 99999 and 7999
    """

    X = X[X.uf17 != 99999]
    X = X[X.uf17 != 7999]
    X = impute_columns(X)
    return X


def impute_columns(X):
    """Replace not reported values with NAN

    Parameters
    ----------
    X : pandas
        original data (unprocessed)

    Returns
    -------
    X : pandas
        removed not reported values
    """

    columns = ['sc24','sc36','sc37','sc38','sc54','sc147','sc174','sc185','sc197',\
        'sc198','sc188','sc571','sc189','sc191','sc193','sc196','sc199',\
        'rec15','rec53']
    replace = {'sc24': [8],'sc36': [8],'sc37': [8],'sc38': [8],'sc54': [3, 8],\
            'sc147': [3, 8],'sc174': [8],'sc185': [8],'sc197': [4, 8],'sc198': [8],\
            'sc188': [8],'sc571': [5, 8],'sc189': [5, 8],'sc191': [8],'sc193': [9],\
            'sc196': [8],'sc199': [8],'rec15': [10, 11, 12],'rec53': [9]}

    for i in columns:
        for key in replace:
            for val in replace[key]:
                # print(key, val)
                X.ix[X[key] == val, key] = math.nan
                # print(i, X[i].value_counts())
    return X