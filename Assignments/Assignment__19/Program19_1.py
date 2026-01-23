#######################################################################################
#   Function name   :   SquareNum
#   Description     :   Returns square of given number
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

SquareNum = lambda No : No*No     

def main():
    Ret = 0
    No = int(input("Enter a number :"))
    Ret = SquareNum(No)
    print(Ret)  
    

if __name__ == "__main__":
    main()