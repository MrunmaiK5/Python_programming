import threading
import time
   
def SumEven(No):
    arr = No
    sum = 0
    for i in arr:
        sum = sum + i

    print("Even sum is: ",sum)

def SumOdd(No):
    sum = 0
    for i in range(1,No+1,2):
        sum = sum + i

    print("Odd sum is: ",sum)

def main():
    start_time = time.time()
    brr = [10,32,21,46,77,43]
    t1 = threading.Thread(target=SumEven, args=(100000000,))

    t2 = threading.Thread(target=SumOdd, args=(100000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.time()

    print("Execution time: ",(end_time-start_time))

if __name__ == "__main__":
    main()