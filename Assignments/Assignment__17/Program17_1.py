
import Arithmetic

def main():
    Ret = 0
    
    Ret = Arithmetic.Add(21,11)
    print("Addition :",Ret)

    Ret = Arithmetic.Sub(21,11)
    print("Subtraction :",Ret)

    Ret = Arithmetic.Mult(21,11)
    print("Muliplication :",Ret)

    Ret = Arithmetic.Div(21,11)
    print("Division :",Ret)

if __name__ == "__main__":
    main()