def ReverseNum(a):
    num = 0
    Digit = 0
    while a > 0:
        Digit = a % 10 
        num = (num*10 ) + Digit
        a = int(a / 10)

    return num


def main():
    Ret = ReverseNum(123)
    print("Reverse number is :", Ret)

if __name__ == "__main__":
    main()