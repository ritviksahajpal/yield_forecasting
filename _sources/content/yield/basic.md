# Basic Crop Yield Forecasting Model

How can we best estimate crop yields? Should we use satellite data or would a simple trend analysis suffice? Based on 
[Johnson et al., 2021](https://www.mdpi.com/2072-4292/13/21/4227), we attempt to answer this question here:
Three linear regression modeling methods were examined and performed identically. The models were fit at the administrative 1 level. The 
predictor variable for the first model was year, monthly maximum NDVI for the second. and area under the NDVI curve for the third model. 
To test the validity of the model's different metrics were used such as the Mean Squared Error (MSE), Mean Absolute Error (MAE), and Coefficient of 
Determination (R-Squared). Each method is explained more in detail in the following subsections.

If you are using google colab to execute the code and your data is stored in the google drive, then execute the 
following code first to connect to google drive:
```python
from google.colab import drive
drive.mount('/content/drive')
```


```python
import pandas as pd
import numpy as np
import datetime
```

Read the csv file with the data as df and start the data cleaning process. Here we set the crop calendar greater than 0 to make sure 
that the crop is actively growing. We then rescale the NDVI values to be between 0 and 1 using the following formula formula: 
Rescaled NDVI = (NDVI - 50)/200. 
```python
# Read in data, compute features, train model
df = pd.read_csv('/content/drive/PATH_TO_DATA.csv')

# Subset to when crop is actively growing i.e. crop_cal != 0
df = df[df['crop_cal'] > 0]

# Rescale the NDVI to be between 0 and 1
df['ndvi'] = (df['ndvi'] - 50)/200

# Subset to the following columns: adm1_name, datetime, yield, ndvi
df = df[['adm1_name', 'datetime', 'yield', 'ndvi','Season']]

# Feature generation: perform a groupby to obtain a dataframe with maximum NDVI value for each admin 1 in each season
df_ml = df.groupby(['adm1_name','Season']).agg({'ndvi':'max','yield':'mean'}).reset_index()

# Drop rows that have missing NDVI or Yield data
df_ml = df_ml.dropna(subset=['yield', 'ndvi'])

# show dataframe
df_ml
```

To create a model, we must train it using part of the data and test the model on a different portion of the data. 
A good way to do this is to split the data into 80% training and 20% testing using `train_test_split` function from Scikit-learn.
```python
# Split the dataframe such that we use 80% of the data for training and predict the remaining 20%
from sklearn.model_selection import train_test_split
train, test = train_test_split(df_ml, test_size=0.2)
test
```

## Model 1: Yield as  function of Year  
For this model, Season (representing year) is the independent variable. So we will call the X values of the training data the Season column, 
and the dependent variable of the training data will be yield. Similarly, we will use Season as the X_test values and the yield is y_test. 
```python
feature_names = ['Season']
X = train[feature_names].values       # training feature matrix
y = train['yield'].ravel()            # training target array
X_test = test[feature_names].values   # test feature matrix
y_test = test['yield'].ravel()        # test target array
```

Next we fit the model linearly with the X as Season and y as yield. 
```python
# Instantiate a Linear Regression Model
from sklearn.linear_model import LinearRegression
model = LinearRegression()

# Fit the model
model.fit(X, y)
```

Now we predict the data based on the model we just created, and the model will give its predictions of the 20% of the tested data using X_test.
```python
# Predict based on the model
y_pred = model.predict(X_test)
y_pred
```

The linear model has an intercept which represents yield if the Season is 0, and a coefficient which is the slope of the relationship between Season and Yield. 
The following line will show the model intercept and coefficient.
```python
# Show model intercept and coefficient
print(model.intercept_, model.coef_)
```

Finally we print all the metrics that measure the validity of our model: Mean Absolute Error, Mean Squared Error and Coefficient of Determination (R-Squared). 
```python
# Estimate model performance using different metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print(f'Coefficient: {model.coef_}')
print(f'Mean Absolute Error: {mean_absolute_error(y_test, y_pred)}')
print(f'Mean Squared Error: {mean_squared_error(y_test, y_pred)}')
print(f'Coefficient of Determination: {model.score(X, y)}')
```

Another way to show the results is using statsmodels.api. This library gives us different metrics about the model, but it presumes the 
intercept is zero. So, we must add sm.add_constant(X) to ensure the results are accurate.
```python
# Show OLS Regression Results using Statsmodel
import statsmodels.api as sm
X = sm.add_constant(X)
statsmodel=sm.OLS(y, X)
results = statsmodel.fit()

print(results.summary())
```

```python
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.019
Model:                            OLS   Adj. R-squared:                  0.007
Method:                 Least Squares   F-statistic:                     1.589
Date:                Tue, 19 Jul 2022   Prob (F-statistic):              0.211
Time:                        19:44:16   Log-Likelihood:                -97.107
No. Observations:                  82   AIC:                             198.2
Df Residuals:                      80   BIC:                             203.0
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const        -52.1156     42.431     -1.228      0.223    -136.556      32.325
x1             0.0266      0.021      1.260      0.211      -0.015       0.069
==============================================================================
Omnibus:                        8.344   Durbin-Watson:                   2.319
Prob(Omnibus):                  0.015   Jarque-Bera (JB):                6.338
Skew:                           0.563   Prob(JB):                       0.0420
Kurtosis:                       2.233   Cond. No.                     9.64e+05
==============================================================================
```
For 2002-2016 the maize yield of each month was linearly regressed against the corresponding month. For the linear regression model, 
80% of the data was used for training of the model while 20% was used for testing. The MAE of this model is 0.69 while the MSE is 0.67. 
The R-squared value is 0.01 which means that 1% of the variance yield is explained by the variance in the months.

## Model 2: Yield as a function of maximum NDVI
For this model, peak NDVI is the independent variable. So we will call the X values of the training data the NDVI column,
and the dependent variable of the training data will be yield. Similarly, we will use peak NDVI as the X_test values and the yield is y_test. 
```python
feature_names = ['ndvi']
X = train[feature_names].values       # training feature matrix
y = train['yield'].ravel()            # training target array
X_test = test[feature_names].values   # test feature matrix
y_test = test['yield'].ravel()        # test target array
```

```python
# Fit the model
model.fit(X, y)
```

Now we predict the data based on the model we just created.
```python
# Predict based on the model
y_pred = model.predict(X_test)
y_pred
```

```python
# Show model intercept and coefficient
print(model.intercept_, model.coef_)
```

```python
# Estimate model performance using different metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print(f'Coefficient: {model.coef_}')
print(f'Mean Absolute Error: {mean_absolute_error(y_test, y_pred)}')
print(f'Mean Squared Error: {mean_squared_error(y_test, y_pred)}')
print(f'Coefficient of Determination: {model.score(X, y)}')
```

```python
# Show OLS Regression Results using Statsmodel
import statsmodels.api as sm
X = sm.add_constant(X)
statsmodel=sm.OLS(y, X)
results = statsmodel.fit()

print(results.summary())
```

```python
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.380
Model:                            OLS   Adj. R-squared:                  0.373
Method:                 Least Squares   F-statistic:                     57.52
Date:                Tue, 19 Jul 2022   Prob (F-statistic):           2.35e-11
Time:                        16:35:22   Log-Likelihood:                -93.315
No. Observations:                  96   AIC:                             190.6
Df Residuals:                      94   BIC:                             195.8
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const         -2.0800      0.466     -4.466      0.000      -3.005      -1.155
x1             5.2793      0.696      7.584      0.000       3.897       6.661
==============================================================================
Omnibus:                        4.677   Durbin-Watson:                   0.620
Prob(Omnibus):                  0.096   Jarque-Bera (JB):                4.504
Skew:                           0.477   Prob(JB):                        0.105
Kurtosis:                       2.534   Cond. No.                         15.2
==============================================================================
```
For 2002-2016 the maximum NDVI was obtained from the time series, and each month’s maize yield was linearly regressed against the maximum
NDVI of the corresponding month. For the linear regression model, 80% of the data was used for training of the model while 20% was used 
for testing. The MAE of this model is 0.61 while the MSE is 0.50. The R-squared value is 0.38 which means that 38% of the variance yield is 
explained by the variance in the peak NDVI. 

## Model 3: Yield as a function of Area under the NDVI curve (AUC)
In this model, we use area under the NDVI curve as a predictor for crop yield. We start by importing the data and applying the crop mask when the 
crop calendar is greater than 1 since we want to measure the accumulated NDVI when the crop is growing. Next we rescale the NDVI to be between 
0 and 1 and subset the data to the columns needed.
```python
df = pd.read_csv('/content/drive/PATH_TO_DATA.csv')

# Subset to when crop is actively growing i.e. crop_cal != 0
df = df[df['crop_cal'] > 1]

# Rescale the NDVI to be between 0 and 1
df['ndvi'] = (df['ndvi'] - 50)/200

# Subset to the following columns: adm1_name, datetime, yield, ndvi
df = df[['adm1_name', 'datetime', 'yield', 'ndvi','Season', 'Month']]
```
Since the datetime column is given as a string, it would be helpful for us to convert that to datetime format.
```python
# Change datetime column from data type str to a datetime
df['datetime'] = pd.to_datetime(df['datetime'])
```
This groupby function is similar to the groupby used in models 1 and 2. However, this time we are not grouping only by region and season, but also by month.
```python
# Calculating Peak NDVI by month
df_ac = df.groupby(['adm1_name','Season','Month']).agg({'ndvi':'max','yield':'mean'}).reset_index()
```
We start calculating the area under the NDVI curve by inserting a column to fill in with those values later.
```python
# Inserting empty column to fill with AUC NDVI values later
df_ac.insert(4,'auc_NDVI','')
```

```python
# Calculating accumulated NDVI
import scipy.integrate as integrate
df_temp = df_ac.groupby(['adm1_name','Season']).apply(lambda x: integrate.trapz(x['ndvi'].values, x = x['Month'].values)).reset_index()
```

To find the area under a curve we must integrate the function used to draw this curve from a starting point to an ending point. 
Similarly, to find the area under the NDVI curve, we will use the beginning of each season as the starting point and the ending of the season as the ending point.
```python
df_ac = df_ac.groupby(['adm1_name','Season']).agg({'accu_ndvi':'max','yield':'mean'}).reset_index() # Grouping rows of NDVI by Region and Season to find NDVI.
df_ac['accu_ndvi'] = df_temp[0] # setting the column of AUC NDVI values in df_ac equal to the calculated accumulated NDVI values
round(df_ac, 2) # Rounding the whole dataset to two decimal places.
```
To avoid having any errors when running the linear regression model, we drop the missing values.
```python
df_ac = df_ac.dropna() # dropping missing values
```

```python
# Instantiate a Linear Regression Model
from sklearn.linear_model import LinearRegression
model = LinearRegression()
```

```python
# Split the dataframe such that we use 80% of the data for training and predict the remaining 20%
from sklearn.model_selection import train_test_split
train, test = train_test_split(df_ac,test_size=0.2)
test
```

```python
feature_names = ['accu_ndvi']
X = train[feature_names].values       # training feature matrix
y = train['yield'].ravel()            # training target array
X_test = test[feature_names].values   # test feature matrix
y_test = test['yield'].ravel()        # test target array
```

```python
# Fit the model
model.fit(X, y)
```

```python
# Predict based on the model
y_pred = model.predict(X_test)
y_pred
```

```python
# Show model intercept and coefficient
print(model.intercept_, model.coef_)
```

```python
# Estimate model performance using different metrics
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print(f'Coefficient: {model.coef_}')
print(f'Mean Absolute Error: {mean_absolute_error(y_test, y_pred)}')
print(f'Mean Squared Error: {mean_squared_error(y_test, y_pred)}')
print(f'Coefficient of Determination: {model.score(X, y)}')
```

```python
# Show OLS Regression Results using Statsmodel
import statsmodels.api as sm
X = sm.add_constant(X)
statsmodel=sm.OLS(y, X)
results = statsmodel.fit()

print(results.summary())
```

```python
 OLS Regression Results                            
==============================================================================
Dep. Variable:                      y   R-squared:                       0.770
Model:                            OLS   Adj. R-squared:                  0.767
Method:                 Least Squares   F-statistic:                     268.3
Date:                Tue, 19 Jul 2022   Prob (F-statistic):           2.83e-27
Time:                        17:39:50   Log-Likelihood:                -41.774
No. Observations:                  82   AIC:                             87.55
Df Residuals:                      80   BIC:                             92.36
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const          0.4933      0.071      6.937      0.000       0.352       0.635
x1             0.5578      0.034     16.378      0.000       0.490       0.626
==============================================================================
Omnibus:                        1.048   Durbin-Watson:                   1.748
Prob(Omnibus):                  0.592   Jarque-Bera (JB):                0.920
Skew:                           0.256   Prob(JB):                        0.631
Kurtosis:                       2.920   Cond. No.                         3.79
==============================================================================
```

## Temporal validation of Model 3
We used an 80-20 train-test split. However, as a result, it is possible that for some years there is data both in the train and the test split.
This results in a bias in the model, also termed as a `data leakage`. To avoid data leakage, we perform temporal validation i.e. the year in the test set
is not in the train set. We repeat the temporal validation for each year in the test set.

```python
#import relevant functions
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

def temporal_validation(df, year):
  # Set aside 1 year as test data, leave all other years for training
  train = df[df['Season'] != year]
  test = df[df['Season'] == year]

  feature_names = ['auc_NDVI']
  X = train[feature_names].values       # training feature matrix
  y = train['yield'].ravel()            # training target array
  X_test = test[feature_names].values   # test feature matrix
  y_test = test['yield'].ravel()

  #Instantiate model
  model = LinearRegression() 

  # Fit the model
  model.fit(X, y)
  
  # Predict based on the model
  y_pred = model.predict(X_test)
  
  #Calculate all metrics in a dataframe friendly format for simple viewing
  stat_array = pd.DataFrame(index=[year],columns=['Intercept','Coefficient', 'Mean Absolute Error', 'Mean Squared Error', 'Coefficient of Determination'])
  stat_array.loc[year,'Intercept'] = model.intercept_
  stat_array.loc[year, 'Coefficient'] = model.coef_
  stat_array.loc[year, 'Mean Absolute Error'] = mean_absolute_error(y_test, y_pred)
  stat_array.loc[year, 'Mean Squared Error'] = mean_squared_error(y_test, y_pred)
  stat_array.loc[year, 'Coefficient of Determination'] =  model.score(X,y)

  return stat_array
```

```python
#Calculate and view temporal validation results
years = np.arange(2002, 2017, 1) #array of all yields where there is data
results = pd.DataFrame() #empty dataframe that results of temp validation will be appended to
for year in years: 
  stat_array = temporal_validation(df_ac, year) #build model for each year and calculate statistics
  results = results.append(stat_array) 

#view results
results
```

```{admonition} Questions
1. Repeat all the 4 models above for each of the following countries:  
    a. Malawi  
    b. Zambia  
    c. Rwanda  
    d. United Republic of Tanzania  
    
    Put all the results from the 4 models and 5 countries in a table and compare them?

2. Use a Random Forest model instead of linear regression for all 4 models and 5 countries. What are the results?  

HINT 1: A random forest regressor is non-parametric model and does not have any coef_ and intercept_ attributes.  

HINT 2:  
from sklearn.ensemble import RandomForestRegressor  
model = RandomForestRegressor(n_estimators=250, random_state=0)  

3. Which model performs better and under what conditions?  
``` 

