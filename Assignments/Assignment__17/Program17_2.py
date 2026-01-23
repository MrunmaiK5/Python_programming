#######################################################################################
#   Function name   :   Display
#   Description     :   Displays matrix of * as per user input 
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

def Display(No):
    for i in range(No):
        for j in range(No):
            print("*", end="\t")
        print()

def main():
    No = 0
    No = int(input("Enter a number :"))
    Display(No)

if __name__ == "__main__":
    main()