def CheckEven(No):
    return (No%2 == 0)

def main():
    Data = [11,10,15,20,22,27,30]

    print("Actual data is: ", Data)

    # filter should give such a function which accepts only one input and give boolean
    FData = list(filter(CheckEven, Data))   # if not converted to list it gives id of location where the filtered data is stored
    print("Data after filter is:",FData)

if __name__ == "__main__":
    main() 