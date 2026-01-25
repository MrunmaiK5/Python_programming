import threading

#######################################################################################
#   Function name   :   EvenList
#   Description     :   Displays additon of even numbers from given list
#   Input           :   List
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def EvenList(Arr):
    Sum = 0
    for i in Arr:
        if i%2 == 0:
            Sum = Sum + i
    
    print("Addition of even list is :",Sum)

#######################################################################################
#   Function name   :   OddList
#   Description     :   Displays additon of odd numbers from given list
#   Input           :   List
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def OddList(Brr):
    Sum = 0
    for i in Brr:
        if i%2 != 0:
            Sum = Sum + i
    
    print("Addition of odd list is :",Sum)
    
def main(): 

    List1 = [10,21,56,25,64,78,11]

    t1 = threading.Thread(target=EvenList, args=(List1,))
    t1.start()
    t1.join()

    t2 = threading.Thread(target=OddList, args=(List1,))
    t2.start()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()