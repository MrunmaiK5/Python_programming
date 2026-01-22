#######################################################################################
#   Function name   :   AddFactors
#   Description     :   Returns addition of the factors of given numbers
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   22/01/26
#######################################################################################

def AddFactors(No):
    Sum = 0
    for i in range(1,No):
        if(No%i == 0):
            Sum = Sum + i

    return Sum

def main():
    Ret = 0
    No = int(input("Enter a number: "))
    Ret = AddFactors(No)
    print(Ret)

if __name__ == "__main__":
    main()