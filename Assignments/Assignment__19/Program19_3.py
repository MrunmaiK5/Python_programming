#######################################################################################
#   Function name   :   NumInBetween
#   Description     :   Checks if number is in between 70 to 90
#   Input           :   Integer
#   Output          :   Bool
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

NumInBetween = lambda No : (No >= 70 and No <= 90 )

#######################################################################################
#   Function name   :   Increment
#   Description     :   Returns number by incrementing it by 10
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

Increment = lambda No : No+10

#######################################################################################
#   Function name   :   Product
#   Description     :   Returns multiplication of given numbers
#   Input           :   Integer, Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

Product = lambda No1, No2 : No1 * No2

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
    Result = 1

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
    
    FData = list(filterX(NumInBetween, Data))
    print(FData)

    MData = list(mapX(Increment,FData))
    print(MData)

    RData = reduceX(Product,MData)
    print(RData)


if __name__ == "__main__":
    main()