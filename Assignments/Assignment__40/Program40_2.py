import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns

###########################################################################################################
#
#   Function Name   :   main
#   Description     :   Checking performance of model after removing "SleepHours" column
#   Input           :   Nothing
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   24/03/26
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

    print("Predicted values : ")
    print(y_pred)
    print(Border)

    print("Feature importance : ",Model.feature_importances_)

    # Evaluate model performance
    print(Border)

    Result1 = accuracy_score(y_test, y_pred)
    print("Accuracy of model before removing SleepHours is: ",(Result1*100))

    print(Border)

    # Removing SleepHours from dataset

    X = X.drop('SleepHours',axis=1)

    x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size=0.2)

    Model = DecisionTreeClassifier()
    Model.fit(x_train,y_train)
    y_pred = Model.predict(x_test)

    print(Border)

    Result2 = accuracy_score(y_test, y_pred)
    print("Accuracy of model after removing SleepHours is: ",(Result2*100))

    print(Border)


if __name__ == "__main__":
    main()