#######################################################################################
#   Function name   :   MinElements
#   Description     :   Returns smallest element of list
#   Input           :   List
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

def MinElements(Arr):
    Min = Arr[0]

    for num in Arr:
        if Min > num:
            Min = num

    return Min
    

def main():
    Ret = 0
    List = list()
    
    No = int(input("Enter size of list: "))

    print("Enter elements: ")
    for i in range(No):
        List.append(int(input()))

    print("List: ",List)

    Ret = MinElements(List)
    
    print("Minimum :",Ret)

if __name__ == "__main__":
    main()