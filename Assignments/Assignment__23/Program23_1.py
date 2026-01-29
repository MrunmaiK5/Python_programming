
#####################################################################################################
#   Class name      :   BookStore
#   Description     :   Class contains two instance variables and one instance method Display 
#                       and one class variable, to display books name author and number of books
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   30/01/26
#####################################################################################################

class BookStore:
    NoOfBooks = 0

    def __init__(self, A, B):
        self.Name = A
        self.Author = B
        BookStore.NoOfBooks += 1

    def Display(self):
        print("Book name :",self.Name," by Author :",self.Author,". No. of books :",BookStore.NoOfBooks)
        print()

obj1 = BookStore("Atomic habits","James clear")
obj1.Display()
obj2 = BookStore("Programming in C","Ajay Mittal")
obj2.Display()
obj3 = BookStore("Scret","Rhonda Byrne")
obj3.Display()


