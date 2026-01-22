#######################################################################################
#   Function name   :   MaxElements
#   Description     :   Returns largest element of list
#   Input           :   List
#   Output          :   Integer
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

def MaxElements(Arr):
    Max = Arr[0]

    for num in Arr:
        if Max < num:
            Max = num

    return Max
    

def main():
    Ret = 0
    List = list()
    
    No = int(input("Enter size of list: "))

    print("Enter elements: ")
    for i in range(No):
        List.append(int(input()))

    print("List: ",List)

    Ret = MaxElements(List)
    
    print("Maximum :",Ret)

if __name__ == "__main__":
    main()