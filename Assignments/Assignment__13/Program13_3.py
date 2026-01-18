#######################################################################################
#   Function name   :   PerfectNo
#   Description     :   Checks whether given number is a perfect number 
#   Input           :   Integer
#   Output          :   Boolean
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   18/01/26
#######################################################################################

def PerfectNo(No):
    Sum = 0
    for i in range(1,No):
        if No%i == 0:
            Sum = Sum + i
    
    if No == Sum:
        return True
    else:
        return False


def main():
    Ret = False
    Ret = PerfectNo(6)

    if Ret == True:
        print("Perfect number")
    else:
        print("Not perfect number")

if __name__ == "__main__":
    main()