def CountDigits(a):
    Count = 0
    while a > 0:
        a = int(a/10)
        Count = Count + 1

    return Count


def main():
    Ret = CountDigits(1234567)
    
    print("No. of digits are :",Ret)

if __name__ == "__main__":
    main()