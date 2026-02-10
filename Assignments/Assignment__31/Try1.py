import schedule
import os
import sys

def DirectoryRename(DictName, OriginalExt, NewExt):
    
    try:

        if (os.path.exists(DictName) == True):
            if(os.path.isdir(DictName) == True):

                for dir, subdir, files in os.walk(DictName):
                    for file in files:
                        name = file.split('.')
                        if OriginalExt == name[1]:
                            file = file.replace(OriginalExt,NewExt)
                            print(file)
            else:
                print("Please enter correct folder name")

        else:
            print("The dirsctory does not exists")       

    except:
        print("Unable to create log file")

def main():
    print(len(sys.argv))
    if(len(sys.argv) != 4):
        print("Please eneter correct arguments")
        print("1 : Folder name")
        print("2 : Extension1")
        print("3 : Extension2")
        return
    else:
        DirectoryRename(sys.argv[1],sys.argv[2],sys.argv[3])
    

if __name__ == "__main__":
    main()