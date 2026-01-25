import threading

#######################################################################################
#   Function name   :   EvenNum
#   Description     :   Prints first 10 even numbers
#   Input           :   Nothing
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def EvenNum():
    print("Odd numberes :")
    for i in range(2,21):
        if i%2 == 0:
            print(i, end="\t")
    print()

#######################################################################################
#   Function name   :   OddNum
#   Description     :   Prints first 10 odd numbers
#   Input           :   Nothing
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def OddNum():
    print("Even numberes :")
    for i in range(20):
        if i%2 != 0:
            print(i, end="\t")
    
def main(): 
    t1 = threading.Thread(target=EvenNum)
    t1.start()
    t1.join()

    t2 = threading.Thread(target=OddNum)
    t2.start()
    t2.join()


if __name__ == "__main__":
    main()