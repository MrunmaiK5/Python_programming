def OddNum(a):
    for i in range(1,a+1):
        if i%2 != 0:
            print(i)

def main():
    OddNum(15)

if __name__ == "__main__":
    main()