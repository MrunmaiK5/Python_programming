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