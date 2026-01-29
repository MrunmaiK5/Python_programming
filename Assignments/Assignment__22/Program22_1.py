
##############################################################################################
#   Class name      :   Demo
#   Description     :   Class contains two instance variables and two instance methods
#                       fun() and gun() and one class variable, to demonstrate oop in python
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   29/01/26
##############################################################################################

class Demo:
    Value = 0

    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B

    def fun(self):
        print("no1 :",self.no1," no2 :",self.no2)

    def gun(self):
        print("no1 :",self.no1," no2 :",self.no2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.fun()
obj2.fun()

obj1.gun()
obj2.gun()