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
#   Description     :   Calculating accuracy without using built-in method 
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

    # Model Building
    Model = DecisionTreeClassifier()

    # Training model
    Model.fit(x_train,y_train)

    # Testing model
    y_pred = Model.predict(x_test)
    print(Border)
    print("Actual values : ")
    print(y_test)
    print()

    print("Predicted values : ")
    print(y_pred)
    print(Border)

    # Evaluate model performance
    print(Border)

    y_test = y_test.to_numpy()


    Sum = 0
    for i in range(len(y_pred)):
        if y_pred[i] == y_test[i]:
            Sum = Sum + 1

    Accuracy = (Sum/len(y_test))

    print("Accuracy without built in : ",Accuracy*100)

    Accuracy_built = accuracy_score(y_test, y_pred)
    print("Accuracy with built in : ",Accuracy_built*100)
    

if __name__ == "__main__":
    main()