#######################################################################################
#   Function name   :   DigitCount
#   Description     :   Counts digits in number
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   22/01/26
#######################################################################################

def DigitCount(No):
    iCnt = 0

    while No > 0:
        No=int(No/10)
        iCnt+=1

    return iCnt
    

def main():
    Ret = 0
    No = int(input("Enter a number: "))

    Ret = DigitCount(No)
    
    print(Ret)

if __name__ == "__main__":
    main()