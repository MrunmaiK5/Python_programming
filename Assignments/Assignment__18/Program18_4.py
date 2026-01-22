#######################################################################################
#   Function name   :   Frequency
#   Description     :   Returns how many times given element appear in list
#   Input           :   List, Integer
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

def Frequency(Arr,No):
    Count = 0

    for num in Arr:
        if No == num:
            Count += 1

    return Count

def main():
    Ret = 0
    List = list()
    
    Size = int(input("Enter size of list: "))

    print("Enter elements: ")
    for i in range(Size):
        List.append(int(input()))

    No = int(input("Enter element to search: "))

    print("List: ",List)

    Ret = Frequency(List,No)
    
    print("Frequency :",Ret)

if __name__ == "__main__":
    main()