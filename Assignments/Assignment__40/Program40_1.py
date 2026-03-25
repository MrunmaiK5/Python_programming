import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns

###########################################################################################################
#
#   Function Name   :   main
#   Description     :   Display importance of each feature
#   Input           :   Nothing
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   24/03/26
#
###########################################################################################################

def main():

    Border = "-"*40

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
    print("Null entries : ",df.isnull().sum())
    print(Border)

    # Splitting variables

    feature_cols = [
        "StudyHours",
        "Attendance",
        "PreviousScore",
        "AssignmentsCompleted",
        "SleepHours",
    ]


    # Visualization 
    sns.scatterplot(x=["StudyHours"],y=["FinalResult"])
    plt.show()

    print(Border)

    X= df[feature_cols]
    Y = df["FinalResult"]

    x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=42, test_size=0.2)

    print("x_train : ",x_train.shape)
    print("x_test : ",x_test.shape)
    print("y_train : ",y_train.shape)
    print("y_test : ",y_test.shape)
    print(Border)

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

    print(Model.feature_importances_)
    # # Evaluate model performance
    # print(Border)

    # Result = accuracy_score(y_test, y_pred)
    # print("Accuracy of model is: ",(Result*100))

    # print(Border)

    # # confusion matrix
    # print(Border)
    # cm = confusion_matrix(y_test, y_pred)

    # print("Confusion matrix : ")
    # data = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=Model.classes_)
    # data.plot()

    # plt.show()

    # print(Border)

if __name__ == "__main__":
    main()