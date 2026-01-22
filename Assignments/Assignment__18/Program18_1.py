#######################################################################################
#   Function name   :   AddElements
#   Description     :   Adds elements of list
#   Input           :   List
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

def AddElements(Arr):
    Sum = 0

    for num in Arr:
        Sum += num

    return Sum
    

def main():
    Ret = 0
    List = list()
    
    No = int(input("Enter size of list: "))

    print("Enter elements: ")
    for i in range(No):
        List.append(int(input()))

    print("List: ",List)

    Ret = AddElements(List)
    
    print("Addition :",Ret)

if __name__ == "__main__":
    main()