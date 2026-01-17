def Factorial(a):
    fact = 1
    for i in range(1,a+1):
        fact = fact * i
    print(fact)

def main():
    Factorial(5)

if __name__ == "__main__":
    main()