
#####################################################################################################
#   Class name      :   Numbers
#   Description     :   Class contains four instance methods ChkPrime, ChkPerfect, Factors, 
#                       SumOfFactors to check if itsprime or perfect and its factors and their sum.
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   30/01/26
#####################################################################################################

class Numbers:
    Value = 0

    def __init__(self,no):
        Numbers.Value = no

    def ChkPrime(self):
        if Numbers.Value <= 1:
            return False
        
        for i in range(2,Numbers.Value):
            if Numbers.Value%i == 0:
                break

        if i >= Numbers.Value-1:
            return True
        else:
            return False

    def ChkPerfect(self):
        Sum = 0
        for i in range(1, Numbers.Value):
            if Numbers.Value%i == 0:
                Sum+=i
        
        if Numbers.Value == Sum:
            return True
        else:
            return False

    def Factors(self,):
        print("Factors of no are :")
        for i in range(1, Numbers.Value+1):
            if Numbers.Value%i == 0:
                print(i)

    def SumFactors(self):
        Sum = 0
        for i in range(1, Numbers.Value+1):
            if Numbers.Value%i == 0:
                Sum+=i

        return Sum

obj1 = Numbers(12)

if obj1.ChkPerfect() == True:
    print("It is an perfect number")
else:
    print("It is not a perfect number")

if obj1.ChkPrime() == True:
    print("It is an prime number")
else:
    print("It is not a prime number")

obj1.Factors()


print("Sum of factors :",obj1.SumFactors())

obj2 = Numbers(7)

if obj2.ChkPerfect() == True:
    print("It is an perfect number")
else:
    print("It is not a perfect number")

if obj2.ChkPrime() == True:
    print("It is an prime number")
else:
    print("It is not a prime number")

obj2.Factors()

print("Sum of factors :",obj2.SumFactors())