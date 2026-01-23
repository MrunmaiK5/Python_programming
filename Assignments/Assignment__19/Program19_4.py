#######################################################################################
#   Function name   :   EvenNum
#   Description     :   Checks if number is even or not
#   Input           :   Integer
#   Output          :   Bool
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

EvenNum = lambda No : (No%2 == 0)

#######################################################################################
#   Function name   :   Square
#   Description     :   Returns square of given number
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

Square = lambda No : No*No

#######################################################################################
#   Function name   :   Add
#   Description     :   Returns Addition of given numbers
#   Input           :   Integer, Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

Add = lambda No1, No2 : No1 + No2

#######################################################################################
#   Function name   :   filterX
#   Description     :   Returns elements from list that satisfy the condition  
#   Input           :   List, Function
#   Output          :   List
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

def filterX(task, Arr):
    Result = list()

    for num in Arr:
        if task(num) == True:
            Result.append(num)

    return Result

#######################################################################################
#   Function name   :   mapX
#   Description     :   Returns elements by appying same function to each
#   Input           :   List, Function
#   Output          :   List
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

def mapX(task, Arr):
    Result = list()

    for num in Arr:
        Result.append(task(num))

    return Result

#######################################################################################
#   Function name   :   reduceX
#   Description     :   Applies function to reduce iterable into single value
#   Input           :   List, Function
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

def reduceX(task, Arr):
    Result = 0

    for num in Arr:
        Result = task(Result,num)

    return Result

def main():
    Ret = 0
    Data = list()

    size = int(input("Enter number of elements in list :"))

    print("Enter elements :")
    for i in range(size):
        Data.append(int(input()))
    
    FData = list(filterX(EvenNum, Data))
    print(FData)

    MData = list(mapX(Square,FData))
    print(MData)

    RData = reduceX(Add,MData)
    print(RData)


if __name__ == "__main__":
    main()