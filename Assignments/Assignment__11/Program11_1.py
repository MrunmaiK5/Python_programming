def IsPrime(a):
    bFlag = False
    for i in range(2,a):
        if a % i == 0:
            bFlag=True
            break

    return bFlag


def main():
    Ret = IsPrime(11)
    
    if Ret == True:
        print("It is not a prime number")
    else:
        print("It is a prime number")

if __name__ == "__main__":
    main()