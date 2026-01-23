#######################################################################################
#   Function name   :   Display
#   Description     :   Displays matrix of number 
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

'''''

    input :     5

    output:     1   
                1   2   
                1   2   3   
                1   2   3   4   
                1   2   3   4   5

'''''

def Display(No):
    for i in range(1,No+1):
        for j in range(1,No+1):
            if i >= j:
                print(j, end="\t")
        print()

def main():
    No = 0
    No = int(input("Enter a number :"))
    Display(No)

if __name__ == "__main__":
    main()