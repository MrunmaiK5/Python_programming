#######################################################################################
#   Function name   :   CheckNum
#   Description     :   Checks whether given number is positive or negative or zero
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   22/01/26
#######################################################################################

def CheckNum(No):
    if No > 0:
        print("Positive Number")
    elif No < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    CheckNum(11)
    CheckNum(-4)
    CheckNum(0)

if __name__ == "__main__":
    main()