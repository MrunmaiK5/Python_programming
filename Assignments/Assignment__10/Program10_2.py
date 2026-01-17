def SumOfNNumbers(a):
    sum = 0
    for i in range(1,a+1):
        sum = sum + i
    print(sum)

def main():
    SumOfNNumbers(5)

if __name__ == "__main__":
    main()