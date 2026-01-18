def IsPalindrome(a):
    original = a
    num = 0
    Digit = 0
    while a > 0:
        Digit = a % 10 
        num = (num*10 ) + Digit
        a = int(a / 10)

    if original == num:
        return True
    else:
        return False


def main():
    Ret = IsPalindrome(121)
    
    if Ret == True:
        print("It is Palindrome")
    else:
        print("It is not a Palindrome")

if __name__ == "__main__":
    main()