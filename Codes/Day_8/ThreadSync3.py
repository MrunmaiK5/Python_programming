import threading

iCnt=0
lobj = threading.Lock()

def Update():
    global iCnt
    for _ in range(2000000):     #i dont want to use i so just told dont allocate memory for local variable
        with lobj:               
            iCnt=iCnt+1

def main():
    global iCnt 

    t1 = threading.Thread(target = Update)
    t2 = threading.Thread(target = Update)

    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

    print("Value of iCnt is :",iCnt)

if __name__ == "__main__":
    main()