import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns

###########################################################################################################
#
#   Function Name   :   main
#   Description     :   Training model using different random_state and comparing the accuracy
#   Input           :   Nothing
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   25/03/26
#
###########################################################################################################

def main():

    Border = "-"*70

    # Load dataset

    print(Border)

    DatasetPath = "student_performance_ml.csv"

    df = pd.read_csv(DatasetPath)

    print("Dataset gets loaded succesfully...")

    print(Border)

    # Analysing data

    print("Shape of dataset : ",df.shape)
    print("Dataset : ")
    print(df.head())
    print("Null entries : ")
    print(df.isnull().sum())
    print(Border)

    # Splitting variables

    X= df.drop("FinalResult",axis = 1)
    Y = df["FinalResult"]

    x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size=0.2)

    # Model2 Building
    Model1 = DecisionTreeClassifier(random_state=0)

    # Training model
    Model1.fit(x_train,y_train)

    # Testing model
    y_pred = Model1.predict(x_test)

    # Evaluate model performance
    print(Border)

    Accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy with random_state=0 : ",Accuracy*100)

    # Model2 Building
    Model2 = DecisionTreeClassifier(random_state=10)

    # Training model
    Model2.fit(x_train,y_train)

    # Testing model
    y_pred = Model2.predict(x_test)

    # Evaluate model performance
    print(Border)

    Accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy with random_state=10 : ",Accuracy*100)


    # Model3 Building
    Model3 = DecisionTreeClassifier(random_state=42)

    # Training model
    Model3.fit(x_train,y_train)

    # Testing model
    y_pred = Model3.predict(x_test)

    # Evaluate model performance
    print(Border)

    Accuracy = accuracy_score(y_test, y_pred)
    print("Accuracy with random_state=42 : ",Accuracy*100)
    

if __name__ == "__main__":
    main()