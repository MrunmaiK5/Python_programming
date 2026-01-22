#######################################################################################
#   Function name   :   IsPrime
#   Description     :   Checks whether given number is prime r not
#   Input           :   Integer
#   Output          :   Bool
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   22/01/26
#######################################################################################

def IsPrime(No):
    for i in range(2,No):
        if(No%i == 0):
            break

    if i >= No-1 :
        return True
    else:
        return False

def main():
    Ret = 0
    No = int(input("Enter a number: "))

    Ret = IsPrime(No)
    
    if Ret == True:
        print("It is a prime number")
    else:
        print("It is not a prime number")

if __name__ == "__main__":
    main()