# importing pandas and numpy

import pandas
import numpy

#Loading Salary_Data dataset
data = pandas.read_csv("Salary_Data.csv")

#Independent Var - Predictor Value
x= data['YearsExperience'].values.reshape(30,1)

#Dependent Var -  Target Value
y= data["Salary"]

#Importing Linear Regression Function
from sklearn.linear_model import LinearRegression

#LR Model Creation Step
print("\n\t\tCreating model.....")
model = LinearRegression()

print("\n\t\tTraining Model .........")
#Model Training Step
model.fit(x,y)

#Prediction
value = int(input("\n\t\tHow much experience employee had ? # "))
data  = model.predict([[value]])

print(f"\n\t\tsalary of {value} years experience candidate is ",data)

#Coefficient 
coeff = model.coef_

print("\n\t\tvalue of coefficient : ", coeff)

print("\n\t\tSaving trained model......")
#To save the model
import joblib
joblib.dump(model, 'Dataset.pk1')
print('\n\t\tModel saved successful !\n')

