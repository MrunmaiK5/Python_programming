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
    return sqrt(((p1['X'] - p2['X']) ** 2) + ((p1['Y'] - p2['Y']) ** 2))

###########################################################################################################
#
#   Function Name   :   main
#   Description     :   KNearestNeighbor Classifer 
#   Input           :   Nothing
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   30/03/26
#
###########################################################################################################

def main():
    Border = "-"*70

    data = [
        {'Point' : 'A', 'X' : 1, 'Y' : 2, 'Label' : 'Red'},
        {'Point' : 'B', 'X' : 2, 'Y' : 3, 'Label' : 'Red'},
        {'Point' : 'C', 'X' : 3, 'Y' : 1, 'Label' : 'Blue'},
        {'Point' : 'D', 'X' : 6, 'Y' : 5, 'Label' : 'Blue'}
    ]

    user_point = {}

    x1 = int(input("Enter x coordinate : "))
    y1 = int(input("Enter Y coordinate : "))

    user_point['X'] = x1
    user_point['Y'] = y1

    for d in data:
        d['distances'] = EucledianD(d, user_point)
    
    
    sorted_data = sorted(data, key=lambda x: x['distances'])


    k = 3
    nearest = sorted_data[:k]

    for d in nearest:
        print(d.get('Point')," - Distance : ",d.get('distances'))

    iMaxr = 0
    iMaxb = 0

    for i in nearest:
        if i.get('Label') == 'Red':
            iMaxr = iMaxr + 1
        else:
            iMaxb = iMaxb + 1
    
    if iMaxr > iMaxb:
        print("Predicted class : Red")
    else:
        print("Predicted class : Blue")

if __name__ == "__main__":
    main()