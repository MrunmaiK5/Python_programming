#######################################################################################
#   Function name   :   Fact
#   Description     :   Returns factorial of a number
#   Input           :   Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   22/01/26
#######################################################################################
def Fact(No):
    factorial = 1
    for i in range(1,No+1):
        factorial = factorial*i

    return factorial

def main():
    Ret = 0
    No = int(input("Enter a number: "))
    Ret = Fact(No)
    print(Ret)

if __name__ == "__main__":
    main()