
##############################################################################################
#   Class name      :   Circle
#   Description     :   Class contains three instance variables and four instance methods
#                       Accept,CalculateArea,CalculateCircumferenceand Display
#                       and one class variable, to calcualte circle's area and circumference
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   29/01/26
##############################################################################################

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self,r):
        self.Radius = r

    def CalculateArea(self):
        self.Area = Circle.PI*(self.Radius*self.Radius)

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius of circle :",self.Radius)
        print("Area of circle :",self.Area)
        print("Circumference of circle :",self.Circumference)
        print()

obj1 = Circle()
obj2 = Circle()
obj3 = Circle()

obj1.Accept(5)
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()

obj2.Accept(12)
obj2.CalculateArea()
obj2.CalculateCircumference()
obj2.Display()

obj3.Accept(20)
obj3.CalculateArea()
obj3.CalculateCircumference()
obj3.Display()