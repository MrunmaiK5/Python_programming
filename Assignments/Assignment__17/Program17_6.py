#######################################################################################
#   Function name   :   Display
#   Description     :   Displays * in triangle pattern
#   Input           :   Integer
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   23/01/26
#######################################################################################

'''''
    input :     5

    output:     *   *   *   *   *
                *   *   *   *
                *   *   *
                *   *
                *
'''''

def Display(No):
    for i in range(1,No+1):
        for j in range(0,(No-i+1)):
            print("*", end="\t")
        print()

    # for i in range(1, No + 1):
    #     for j in range(1, No + 1):
    #         if i <= j:
    #             print("*", end = "\t")
    #     print()

def main():
    No = 0
    No = int(input("Enter a number :"))
    Display(No)

if __name__ == "__main__":
    main()