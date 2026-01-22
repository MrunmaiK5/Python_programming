#######################################################################################
#   Function name   :   EvenDisplay
#   Description     :   Display first 10 even numbers
#   Input           :   Integer
#   Output          :   Bool
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   22/01/26
#######################################################################################

# def EvenDisplay():
#     No = 2
#     for i in range(10):
#         print(No)
#         No+=2

def EvenDisplay():
    for i in range(2,21,2):
        print(i)

def main():
    EvenDisplay()

if __name__ == "__main__":
    main()