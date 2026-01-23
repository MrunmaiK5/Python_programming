#######################################################################################
#   Function name   :   Multiply
#   Description     :   Returns multiplication of given numbers
#   Input           :   Integer, Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

Multiply = lambda No1, No2 : No1*No2     

def main():
    Ret = 0

    No1 = int(input("Enter 1st number :"))
    No2 = int(input("Enter 2nd number :"))

    Ret = Multiply(No1, No2)
    print(Ret)  

if __name__ == "__main__":
    main()