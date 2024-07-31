#This code follows the 7 main steps of creating a machine learning model:
#reading data, cleaning data, splitting the data into a train and test data 
#set, building and training a model, and analyzing the error of the model 
#
#The application used in this code predicts the number of medals 
#an olympic team would recieve based on the number of athletes and the previous 
#number of medals that each team earned 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import numpy as np

#STEP 1: read the data file and determine whether there is any correlation to work
#with in the data set 
teams = pd.read_csv("teams.csv")
teams = teams[["team", "country", "year", "athletes", "age", "prev_medals", "medals"]]
print(teams.corr(numeric_only="true")["medals"])
sns.lmplot(x="athletes", y="medals", data=teams, fit_reg=True, ci=None)

#need this line to show plots that are run outside of the notebook
#will open the plot in a new window and stop the code after it from running 
#too apparently...
#plt.show()

#STEP 2: CLEAN data 
teams = teams.dropna() #drop any rows that have a missing value 

#STEP 3: SPLIT the training and test data set 
train = teams[teams["year"] < 2012].copy()
test = teams[teams["year"] >= 2012].copy()

#tells how much data is in each data set 
print("Training data set ", train.shape)
print("Testing data set ", test.shape)

#STEP 4: TRAIN our model 
reg = LinearRegression()
predictors = ["athletes", "prev_medals"]
target = "medals"
#"training the regression model by fitting the regression "
reg.fit(train[predictors], train["medals"])

#using the regression model to generate a set of predictions given the
#predictors from the test data 
predictions = reg.predict(test[predictors])
test["predictions"] = predictions #assigns the predictions to a column in the test data frame

#STEP 5: CORRECT the output and round the data 
test.loc[test["predictions"] < 0, "predictions"] = 0
test["predictions"] = test["predictions"].round()
print(test)

#analyze the error of our model 
#this error value represents the mean number of medals that our model 
#came within > good check to see whether the error predictor is well 
#within the range of the standard deviation of the entire data set 
error = mean_absolute_error(test["medals"], test["predictions"])
print(error)
print(teams.describe()["medals"])

#printing out the entire column so we can see how close our model came 
#to the actual predictions > notice how mean absolute error can be very 
#different for different countries 
print(test[test["team"] == "USA"])
print(test[test["team"] == "IND"])

#difference between the number of medals predicted and the 
#number of medals that were actually earned by every team 
errors = (test["medals"] - test["predictions"]).abs()
print(errors)
#will group the errors by the team in the team column and calculate the error for each team 
error_by_team = errors.groupby(test["team"]).mean()
print(error_by_team)

medals_by_team = test["medals"].groupby(test["team"]).mean()
error_ratio = error_by_team / medals_by_team 
#CLEAN up missing and null values 
error_ratio[~pd.isnull(error_ratio)]
error_ratio = error_ratio[np.isfinite(error_ratio)]
print(error_ratio) #can use error_ratio.plot.hist() to see what the ratios are 
#INTERPRETATION NOTES: 
        # if the error ratio is between 0 and 0.5, this means that the prediction 
        #was within 50% of the number of medals actually earned 
print(error_ratio.sort_values())

#how to improve this model 
#add more predictors, try different models (random forest, etc)
#