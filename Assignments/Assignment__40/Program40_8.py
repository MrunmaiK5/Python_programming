import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns

###########################################################################################################
#
#   Function Name   :   main
#   Description     :   Plotting tree using plot_tree function
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
    print("Accuracy is : ",Accuracy*100)

    plt.figure(figsize=(7,5))
    plot_tree(Model1, filled=True, feature_names=["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours","FinalResult"])
    plt.show()

if __name__ == "__main__":
    main()