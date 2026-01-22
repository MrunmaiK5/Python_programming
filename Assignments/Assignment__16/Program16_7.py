#######################################################################################
#   Function name   :   IsDivisible
#   Description     :   Checks whether given number is divisible by 5 or not
#   Input           :   Integer
#   Output          :   Bool
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   22/01/26
#######################################################################################

def IsDivisible(No):
    if No%5 == 0:
        return True
    else:
        return False

def main():
    Ret = False
    Ret = IsDivisible(8)

    if Ret == True:
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()