#######################################################################################
#   Function name   :   AreaOfCircle
#   Description     :   Calculates area of circle
#   Input           :   Float
#   Output          :   Float
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   18/01/26
#######################################################################################

def AreaOfCircle(radius):
    Area = 0.0
    Area = float(3.14 * (radius**2))
    return Area


def main():
    Radius = 0.0
    Ret = 0.0

    print("Enter a radius: ")
    Radius = float(input())

    Ret = AreaOfCircle(Radius)
    print("Area is: ",Ret)

if __name__ == "__main__":
    main()