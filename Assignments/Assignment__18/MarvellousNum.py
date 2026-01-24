#######################################################################################
#   Module name     :   MarvellousNum
#   Description     :   Provides a function ChkPrime to check number is prime or not
#   Input           :   Integer
#   Output          :   Bool
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

def ChkPrime(no):
    res = False

    if no <= 1:
        res = False

    for i in range(2,no):
        if no%i == 0:
            res = False
    
    res = True
    
    return res
