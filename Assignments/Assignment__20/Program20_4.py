import threading

#######################################################################################
#   Function name   :   Small
#   Description     :   Displays count of number of small characters in string
#   Input           :   String
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def Small(String):
    threadname = threading.current_thread().name
    print("Thread Id :",threading.get_ident(),"Thread Name :",threadname)
    Count = 0
    for character in String:
        if character >= 'a' and character <= 'z':
            Count = Count+1
    
    print("Count of small characters is :",Count)
    print()

#######################################################################################
#   Function name   :   Capital
#   Description     :   Displays count of number of capital characters in string
#   Input           :   String
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def Capital(String):
    threadname = threading.current_thread().name
    print("Thread Id :",threading.get_ident(),"Thread Name :",threadname)
    Count = 0
    for character in String:
        if character >= 'A' and character <= 'Z':
            Count = Count+1
    
    print("Count of capital characters is :",Count)
    print()

#######################################################################################
#   Function name   :   Digits
#   Description     :   Displays count of number of Digits characters in string
#   Input           :   String
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   26/01/26
#######################################################################################

def Digits(String):
    threadname = threading.current_thread().name
    print("Thread Id :",threading.get_ident(),"Thread Name :",threadname)
    Count = 0
    for digits in String:
        if digits >= '0' and digits <= '9':
            Count = Count+1
    
    print("Count of digits is :",Count)
    print()

def main(): 

    String = "Mrunmai Khadpe 100"

    t1 = threading.Thread(target=Small, args=(String,))
    t2 = threading.Thread(target=Capital, args=(String,))
    t3 = threading.Thread(target=Digits, args=(String,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")

if __name__ == "__main__":
    main()