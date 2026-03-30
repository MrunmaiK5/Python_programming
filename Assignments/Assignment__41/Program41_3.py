from math import sqrt

###########################################################################################################
#
#   Function Name   :   EuclideanD
#   Description     :   Calculates Eucledian distance between two points 
#   Input           :   Dict, Dict
#   Output          :   Float
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   30/03/26
#
###########################################################################################################

def EucledianD(p1, p2):
    return sqrt(((p1['StudyHours'] - p2['StudyHours']) ** 2) + ((p1['Attendance'] - p2['Attendance']) ** 2))

###########################################################################################################
#
#   Function Name   :   main
#   Description     :   using knn to predict if student passes or fails exam
#   Input           :   Nothing
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   30/03/26
#
###########################################################################################################

def main():
    Border = "-"*70

    data = [
        {'StudyHours' : 2, 'Attendance' : 60, 'Result' : 'Fail'},
        {'StudyHours' : 5, 'Attendance' : 80, 'Result' : 'Pass'},
        {'StudyHours' : 6, 'Attendance' : 85, 'Result' : 'Pass'},
        {'StudyHours' : 1, 'Attendance' : 50, 'Result' : 'Fail'}
    ]

    user_point = {}

    x1 = int(input("Enter study hours : "))
    y1 = int(input("Enter attendance : "))

    user_point['StudyHours'] = x1
    user_point['Attendance'] = y1

    for d in data:
        d['distances'] = EucledianD(d, user_point)
    
    
    sorted_data = sorted(data, key=lambda x: x['distances'])

    k = 3
    nearest = sorted_data[:k]

    icntp = 0
    icntf = 0

    for i in nearest:
        if i.get('Result') == 'Pass':
            icntp = icntp + 1
        else:
            icntf = icntf + 1
    
    if icntp > icntf:
        print("Predicted Result -> Pass")
    else:
        print("Predicted Result -> Pass")

if __name__ == "__main__":
    main()