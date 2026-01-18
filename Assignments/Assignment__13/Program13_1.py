def AreaOfRect(Len, Wid):
    Area = 0
    Area = Len * Wid
    return Area


def main():
    Length = 0
    Width  = 0
    Ret = 0

    print("Enter length of a rectangle: ")
    Length = int(input())

    print("Enter width of a rectangle: ")
    Width = int(input())

    Ret = AreaOfRect(Length, Width)
    print("Area is: ",Ret)

if __name__ == "__main__":
    main()