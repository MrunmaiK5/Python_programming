#######################################################################################
#   Function name   :   DigitAdd
#   Description     :   Adds digits in number
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   22/01/26
#######################################################################################

def DigitAdd(No):
    Sum = 0
    Digit = 0

    while No > 0:
        Digit = int(No%10)
        Sum = Sum + Digit
        No=int(No/10)
    
    return Sum
    

def main():
    Ret = 0
    No = int(input("Enter a number: "))

    Ret = DigitAdd(No)
    
    print(Ret)

if __name__ == "__main__":
    main()