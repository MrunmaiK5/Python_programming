#######################################################################################
#   Function name   :   StrlenX
#   Description     :   Display first 10 even numbers
#   Input           :   Integer
#   Output          :   Bool
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   22/01/26
#######################################################################################

def StrlenX(name):
    length = 0
    
    for i in name:
        length = length + 1
        
    return length


def main():
    Ret = 0
    String = "Marvellous"
    Ret = StrlenX(String)
    print("Length: ",Ret)

if __name__ == "__main__":
    main()