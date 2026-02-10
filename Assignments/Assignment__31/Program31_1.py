import schedule
import os
import sys
import time

########################################################################################################
#   Function name   :   DirectoryFileSearch
#   Description     :   Displays files with given extension from given directory name
#   Input           :   String, String
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   10/02/26
########################################################################################################

def DirectoryFileSearch(DictName, Ext):
    
    try: 
        fname = time.strftime("%Y-%m-%d_%H-%M-%S") + ".log"
        
        os.mkdir("P31")
        fname = os.path.join("P31",fname)
        
        fobj = open(fname,"w")

        if (os.path.exists(DictName) == True):
            if(os.path.isdir(DictName) == True):

                for dir, subdir, files in os.walk(DictName):
                    for file in files:
                        name = file.split('.')
                        if Ext == name[1]:
                            fobj.write(file)
                    
                fobj.close()
                print("Successfully written the file names")

            else:
                print("Please enter correct folder name")

        else:
            print("The dirsctory does not exists")       

    except:
        print("Unable to create log file")

def main():
    print(len(sys.argv))
    if(len(sys.argv) != 3):
        print("Please eneter correct arguments")
        print("1 : Folder name")
        print("2 : Extension")
        return
    else:
        
        schedule.every(30).seconds.do(DirectoryFileSearch, sys.argv[1],sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()