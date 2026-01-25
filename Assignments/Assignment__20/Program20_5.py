import threading

#######################################################################################
#   Function name   :   Thread1
#   Description     :   Displays numbers from 1 to 50
#   Input           :   Nothing
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def Thread1():
    print("Thread1:")
    for i in range(1,51):
        print(i, end="\t")
    
    print()

#######################################################################################
#   Function name   :   Thread2
#   Description     :   Displays numbers from 50 to 1 in reverse order
#   Input           :   Nothing
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def Thread2():
    print("Thread2:")
    for i in range(50,0,-1):
        print(i, end="\t")
    
    print()

def main(): 

    t1 = threading.Thread(target=Thread1)
    t1.start()
    t1.join()

    t2 = threading.Thread(target=Thread2)
    t2.start()
    t2.join()


if __name__ == "__main__":
    main()