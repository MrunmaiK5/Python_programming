
#####################################################################################################
#   Class name      :   BankAmount
#   Description     :   Class contains two instance variables and four instance method Display,
#                       Deposit, withdraw, CalculateInterest and one class variable, 
#                       to display basic bank related operations.
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   30/01/26
#####################################################################################################

class BankAccount:
    ROI = 10.5

    def __init__(self, A, B):
        self.Name = A
        self.Amount = B

    def Deposit(self,no):
        self.Amount += no 

    def Withdraw(self,no):
        if self.Amount >= no:
            self.Amount-=no
        else:
            print("Insufficient Balance !!")
            return

    def CalculateInterest(self):
        return ((self.Amount * BankAccount.ROI) / 100)

    def Display(self):
        print("Name :",self.Name,"Remaining Balance :",self.Amount)

obj1 = BankAccount("Sanika",20000)
obj1.Deposit(300)
obj1.Display()
obj1.Withdraw(2301)
obj1.Display()
print("Interest:",obj1.CalculateInterest())

obj2 = BankAccount("Mrunmai",3200)
obj2.Deposit(200)
obj2.Display()
obj2.Withdraw(21)
obj2.Display()
print("Interest:",obj2.CalculateInterest())

obj3 = BankAccount("Shraddha",500)
obj3.Deposit(980)
obj3.Display()
obj3.Withdraw(42)
obj3.Display()
print("Interest:",obj3.CalculateInterest())