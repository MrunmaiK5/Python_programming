#######################################################################################
#   Function name   :   ListPrime
#   Description     :   Returns addition of prime numbers by calling function from
#                       user defined module MarvellousNum
#   Input           :   Nothing
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

import MarvellousNum as mn

def ListPrime():
    Ret = 0
    List = list()
    
    Size = int(input("Enter size of list: "))

    print("Enter elements: ")
    for i in range(Size):
        List.append(int(input()))

    Add = 0
    for num in List:
        if mn.ChkPrime(num) == True:
            Add = Add + num
        
    print("Addition of prime numbers :",Add)

if __name__ == "__main__":
    ListPrime()