# homework-ii-pm2877, homework-ii-vv2269

## Team Members: Parth Mehta(pm2877), Vidya Venkiteswaran(vv2269)

## Steps Involved

### Data Preprocessing:
    1. Removed features manually from the data. These included features related to the householders, previous tenants and all features that were not related to vacant apartments.
    2. Collapsed some columns that have multiple categories to a single feature vector. Example, we created a feature vector called 'score' that collapsed 20 feature columns in the original dataset into a single house score.
	4. Then we used RFE to find the ranks of the remaining features, and removed some more features with low rank, and found that the optimal cross-validation accuracy was obtained with the first 41 ranked features.

Note: The number of rows for borough 5 are only 274, which is very less. The 5th category of boro constituted only 1/5th of the data

### Visualization:
	1. After removing the features, we observed we had only categorical data only. We generated scatterplots and histograms for the remaining columns to visualize the data. We removed columns that have single value, because it wont have any effect on the predictions.

### Data:
	1. Divide data into train and test using scikit's train_test_split
	2. We thought of splitting the data such that the boro could be equally divided (Refer to Note)

### Modeling:
	1. Next, we fitted a LinearRegression model on the training set, and used 5-fold cross-validation to calculate the R^2 accuracy. Then we tried out Lasso which improved our r^2 but when we used ridge it made a significant difference

#### Feature Distribution, Feature Engineering and Modeling
    1. We then created a pipeline and tried a lot of things like various scaling techniques, feature selection techniques like PCA, and various cross-validation strategies. We found that scaling the data did not make any difference, nor did PCA make a huge difference to the cross-validation errors.
    2. We used polynomial features of degree 2 as part of feature engineering which shooted our r^2 to 0.43
    3. We then used SoftImpute with strategy as most frequent and Imputer functions to impute the  8 and 9 category values in the data. 
    4. We then used OneHotEncoding technique to distribute categorical values in the data. This drastically improved our training accuracy.
	5. We also compared results of various regression models and finally found RidgeCV to be the best fit.

Finally, our pipeline consists of OneHOtEncoder and RidgeCV functions.

## Installation
	1. Run pip install -r requirements.txt in your environment
	2. Run homework2_rent.py

## Flow
	1. It downloads the data into the current folder. This is called data.csv
	2. We read the data into a pandas data frame
	3. Then we preprocess the data as described in Data Preprocessing step
	4. We splitted the data into train and test
	5. Created a pipeline as mentioned in step(Feature Distribution and Modeling)
	6. Used this pipeline to fit on training data
	7. This model was then tested on test data

## Files
	1. homework2_rent.py - main file to run
	2. visualization.py - to create scatter plots (step: visualization)
	3. download_data.py -  to download data
	4. pre_processing - for preprocessing as described in step : Data Preprocessing
