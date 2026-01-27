import threading

SharedCounter = 0
lock = threading.Lock()

#######################################################################################
#   Function name   :   Thread1, Thread2, Thread3, Thread4
#   Description     :   Updates the shared counter.
#   Input           :   Nothing
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def Thread1():
    global SharedCounter

    for i in range(10000):
        lock.acquire()
        SharedCounter += 2
        lock.release()

def Thread2():
    global SharedCounter

    for i in range(10000):
        lock.acquire()
        SharedCounter -=1
        lock.release()

def Thread3():
    global SharedCounter

    for i in range(10000):
        lock.acquire()
        SharedCounter += 2
        lock.release()

def Thread4():
    global SharedCounter

    for i in range(10000):
        lock.acquire()
        SharedCounter += 1
        lock.release()

def main(): 
    t1 = threading.Thread(target=Thread1)
    t2 = threading.Thread(target=Thread2)
    t3 = threading.Thread(target=Thread3)
    t4 = threading.Thread(target=Thread3)
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print("Counter :",SharedCounter)

if __name__ == "__main__":
    main()