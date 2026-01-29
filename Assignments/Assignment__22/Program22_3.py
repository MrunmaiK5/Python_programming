
##############################################################################################
#   Class name      :   Arithmetic
#   Description     :   Class contains two instance variables and five instance methods
#                       Accept, Addition, Subtraction, Multplication, Division and 
#                       one class variable, to perform basic Arithmetic operations
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   29/01/26
##############################################################################################

class Arithmetic:
    PI = 3.14

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self,A,B):
        self.Value1 = A
        self.Value2 = B

    def Addition(self):
        return self.Value1+self.Value2

    def Subtraction(self):
        return self.Value1-self.Value2

    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        return self.Value1 / self.Value2

obj1 = Arithmetic()
obj2 = Arithmetic()
obj3 = Arithmetic()

obj1.Accept(21,11)
print("Addition :",obj1.Addition())
print("Subtraction :",obj1.Subtraction())
print("Multiplication :",obj1.Multiplication())
print("Division :",obj1.Division())

obj2.Accept(101,51)
print("Addition :",obj2.Addition())
print("Subtraction :",obj2.Subtraction())
print("Multiplication :",obj2.Multiplication())
print("Division :",obj2.Division())

obj3.Accept(201,11)
print("Addition :",obj3.Addition())
print("Subtraction :",obj3.Subtraction())
print("Multiplication :",obj3.Multiplication())
print("Division :",obj3.Division())