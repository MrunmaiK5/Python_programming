#######################################################################################
#   Function name   :   ChkNum
#   Description     :   Checks whether number is even or odd
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   22/01/26
#######################################################################################

def ChkNum(No):
    if No%2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    ChkNum()

if __name__ == "__main__":
    main()