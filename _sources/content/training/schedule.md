# Schedule August 26 - 30, 2022

## Day 1
|     | **Friday August 26, Day 1/3 - Introduction to Crop Condition Analysis**                         |
|-----|-------------------------------------------------------------------------------------------------|
|     | _Activity_                                                                                      |
| 1.  | Greetings                                                                                       |
| 2.  | Current approach to crop condition and yield analysis in RCMRD                                  |
|     | **BREAK**                                                                                       |
| 3.  | **VIDEO**: How's it Growing?                                                                    |
| 4.  | **VIDEO**: AgMet graphics                                                                       |
| 5.  | How to use AgMet graphics?                                                                      |
| 6.  | **VIDEO**: Using the GLAM system                                                                |
|     | **LUNCH**                                                                                       |
| 7.  | Walkthrough of geoprepare library                                                               |
| 8.  | Walkthrough of key data inputs for geoprepare                                                   |
| 9.  | Initiate assignment                                                                             |
|     | **BREAK**                                                                                       |
| 10. | * Assignment<br/>* Check geoprepare installation on RCMRD and NASA servers with Benson and Sara |

### Assignment
[Day 1 assignment](https://docs.google.com/document/d/1OJ8OLKgkwkwweRfim9aTKz2NFm6P9GLRvgFOaW2WQf0/edit?usp=sharing)

## Day 2
|     | **Monday August 29, Day 2/3 - Crop Condition Analysis**                   |
|-----|---------------------------------------------------------------------------|
|     | _Activity_                                                                |
| 1.  | Review of day 1                                                           
| 2.  | Install [MOBAXTerm](https://mobaxterm.mobatek.net/), access RCMRD cluster |
|     | **BREAK**                                                                 |
| 3.  | Creating a crop condition report                                          |
| 4.  | Assignment                                                                |
|     | **LUNCH**                                                                 |
| 5.  | Building a simple crop yield forecast model                               |
| 6.  | Assignment                                                                |

### Assignment
Link to AgMet and percentile plots: https://www.dropbox.com/sh/40343f0zvyidsbm/AADjkiwtEpLY5bAs395w3rTya?dl=0  
Document: https://docs.google.com/document/d/1Nz5x-R7Kl4DDxZ0uEe453QrhXwci7K8tpu3ZYGl6G4I/edit?usp=sharing  

* Perform crop condition analysis for Kenya, Malawi, Rwanda, Zambia and United Republic of Tanzania using the graphics and questions outlined 
[here](https://ritviksahajpal.github.io/yield_forecasting/content/condition/analysis.html)

* Repeat all the 4 models from [here](https://ritviksahajpal.github.io/yield_forecasting/content/yield/basic.html) for each of the following countries:  
    Malawi  
    Zambia   
    Rwanda   
    United Republic of Tanzania    
Put all the results from the 4 models and 5 countries in a table and compare them.  

* Use a Random Forest model instead of linear regression for all 4 models and 5 countries. What are the results?  
    _HINT 1_:   
    A random forest regressor is non-parametric model and does not have any coef_ and intercept_ attributes.  

    _HINT 2_:  
    ```python
    from sklearn.ensemble import RandomForestRegressor  
    model = RandomForestRegressor(n_estimators=250, random_state=0)
  ```  
Which model performs better and under what conditions?  
