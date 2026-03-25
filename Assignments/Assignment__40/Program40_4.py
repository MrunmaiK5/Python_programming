import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import seaborn as sns

###########################################################################################################
#
#   Function Name   :   main
#   Description     :   Evaluating model's performance for new 5 entries
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

    print("Predicted values : ")
    print(y_pred)
    print(Border)

    # Evaluate model performance
    print(Border)

    Result1 = accuracy_score(y_test, y_pred)
    print("Accuracy of model with all features is: ",(Result1*100))

    print(Border)

    #StudyHours,Attendance,PreviousScore,AssignmentsCompleted,SleepHours,FinalResult
    new_entries ={
        "StudyHours" : [5.0,2.0,1.5,2.3,8.0],
        "Attendance" : [89,65,64,54,80],
        "PreviousScore" : [89,60,68,54,83],
        "AssignmentsCompleted": [9,6,4,5,8],
        "SleepHours" : [8,5,6,7,8],
        "FinalResult" : [1,0,0,0,1]
        }

    ndf = pd.DataFrame(new_entries)

    Xtest = ndf.drop("FinalResult",axis=1)
    Ytest = ndf["FinalResult"]
    
    # Testing model
    Y_pred = Model.predict(Xtest)
    print(Border)
    print("Actual values : ")
    print(Ytest)

    print("Predicted values : ")
    print(Y_pred)
    print(Border)

    # Evaluate model performance
    print(Border)

    Result2 = accuracy_score(Ytest, Y_pred)
    print("Accuracy of model with all features is: ",(Result2*100))


if __name__ == "__main__":
    main()