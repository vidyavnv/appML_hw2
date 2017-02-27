#!/usr/bin/env python

####################################################
# File name: homework2_rent.py                     #
# Author: Parth Mehta, Vidya Venkiteswaran         #
# Email: pm2877@columbia.edu, vv2269@columbia.edu  #
# Date created: 02/26/2017                         #
# Usage: python homework2_rent.py                  #
# Python Version: 3.4, 3.5, 3.6                    #
# Instructor: Prof. Andreas Mueller                #
####################################################

import pandas as pd
import numpy as np

from sklearn import linear_model
from sklearn.model_selection import cross_val_score
from sklearn.cross_validation import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import r2_score
from sklearn.feature_selection import RFE
from sklearn.preprocessing import PolynomialFeatures

from pre_processing import collapse_columns, remove_empty
from download_data import download_data
from visualization import scatter_plot


def pre_process(housing_data):
    """Preprocess data

    Remove columns which have unapplicable data and get
    a score for house feature like stairways, floors, walls,
    and windows. Inaddition to this, drop the target column
    from the data and the columns identified from feature selection

    Parameters
    ----------
    housing_data : pandas
                   housing data from csv

    Returns
    -------
    housing_data
        preprocessed data
    """
    
    housing_data = remove_empty(housing_data)
    housing_data = collapse_columns(housing_data)

    infile = open('headers.txt','r')
    non_selected_features = infile.read().splitlines()
    infile.close()

    housing_data = housing_data.drop(non_selected_features, axis=1)

    housing_X = housing_data.drop('uf17', axis=1)
    housing_Y = housing_data['uf17']

    return housing_X, housing_Y
 
    
def predict_rent():
    """Predict rent of test housing data

    Use the trained model to predict price of test data and
    convert test data into numpy array

    Parameters
    ----------
    None

    Returns
    -------
    test_X           : numpy array
                       test data for housing
    test_Y           : numpy array
                       actual values of test data
    predicted_values : numpy array 
                       predicted values of test data
    
    """

    test_X, test_Y, model = train_model()
    predicted_values = model.predict(predicted_values)
    return test_X.as_matrix(), test_Y.as_matrix(), predicted_values


def score_rent():
    """Return R^2 value between actual and predicted

    Parameters
    ----------
    None

    Returns
    -------
    score
        float
        coefficient of determination between actual and predicted value
    """

    test_X, test_Y, model = train_model()
    predicted_values = model.predict(test_X)
    score = r2_score(predicted_values, test_Y)
    print(score)
    return score


def train_model():
    """Train model using training data

    Download data, preprocess data, split data and create a
    model 

    Parameters
    ----------
    None
    
    Returns
    -------
    test_X : pandas
             test data for the house
    test_Y : pandas
             actual price of the house
    pipe   : sklearn.pipeline.Pipeline
             model built from sklearn
    """

    # download the data from the link
    is_success = download_data()
    if not is_success:
        print("Unable to download the file. Using the already created one")
    # Read data from csv and store it into pandas dataframe
    housing_data = pd.read_csv('data.csv')   
    # Preprocess data 
    housing_X, housing_Y = pre_process(housing_data)
    columns = list(housing_X.columns.values)
    # print(columns)

    # Split data into train and test
    housing_train_X, housing_test_X, housing_train_Y, housing_test_Y = \
        train_test_split(housing_X, 
                         housing_Y, 
                         random_state = 42) 
    # scatter_plot(housing_test_X, housing_test_Y)
    
    # Make pipeline for feature distribution and model
    pipe = make_pipeline(Imputer(), PolynomialFeatures(2), OneHotEncoder(sparse=False, 
                                       handle_unknown='ignore'), 
                         linear_model.RidgeCV())

    # fit the model on training data
    pipe.fit(housing_train_X, housing_train_Y)
    
    return housing_test_X, housing_test_Y, pipe


if __name__ == '__main__':
    score_rent()

