import threading
   
def Display(No):
    print("Inside Display :",No)

def main():
    # args -> (11,) it is a tuple that indicates that it can have more arguments
    # we used keyword argument also supports variable argument
    t = threading.Thread(target=Display, args=(11,))    
    t.start()

if __name__ == "__main__":
    main()