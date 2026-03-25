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
#   Description     :   Adding a new feature "PerformanceIndex" and training the model for its exaluation   
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
    print(df.shape)
    print(type(df))

    PerformanceIndex = []

    for i in range(len(df)):
        PerformanceIndex.append((df["StudyHours"][i] * 2) + df["Attendance"][i])

    PerformanceIndex = pd.DataFrame(PerformanceIndex, columns=["PerformanceIndex"])

    df = pd.concat([df,PerformanceIndex], axis=1)

    
    

if __name__ == "__main__":
    main()