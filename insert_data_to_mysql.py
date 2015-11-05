#! /usr/bin/env python
#coding=utf-8

import csv
import csv as csv
import numpy as np
import db

csv_file_object = csv.reader(open('train.csv', 'rb'))       # Load in the csv file
header = csv_file_object.next()                             # Skip the fist line as it is a header
data=[]                                                     # Create a variable to hold the data

for row in csv_file_object:                 # Skip through each row in the csv file
    data.append(row)                        # adding each row to the data variable


sql = 'insert into titanic_train (PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
db.ExecuteSQLs(sql, data)
