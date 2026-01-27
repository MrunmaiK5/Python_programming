import threading

#######################################################################################
#   Function name   :   EvenFactor
#   Description     :   Displays additon of even factors of given numbers
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def EvenFactor(No):
    Sum = 0
    for i in range(1,No+1):
        if No%i == 0 and i%2 == 0:
            Sum = Sum + i
    
    print("Addition of even factors is :",Sum)

#######################################################################################
#   Function name   :   OddFactor
#   Description     :   Displays additon of odd factors of given numbers
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def OddFactor(No):
    Sum = 0
    for i in range(1,No+1):
        if No%i == 0 and i%2 != 0:
            Sum = Sum + i
    
    print("Addition of odd factors is :",Sum)
    
def main(): 
    t1 = threading.Thread(target=EvenFactor, args=(12,))
    t2 = threading.Thread(target=OddFactor, args=(12,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()