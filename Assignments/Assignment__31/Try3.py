import schedule
import os
import sys
import time

########################################################################################################
#   Function name   :   DirectoryRename
#   Description     :   Displays files by replacing their extension with new extension given by user
#   Input           :   String, String, String
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   10/02/26
########################################################################################################

def DirectoryRename(DictName, OriginalExt, NewExt):

    if (os.path.exists(DictName) == True):
        if(os.path.isdir(DictName) == True):

            for dir, subdir, files in os.walk(DictName):
                for file in files:
                    name = file.split('.')
                    if OriginalExt == name[1]:
                        nfile = file.replace(OriginalExt,NewExt)
                        print(nfile)
                        os.rename(file,nfile)
                        # fobj.write(file)
                
            # fobj.close()
            print("Successfully written the file names")


def main():
    print(len(sys.argv))
    if(len(sys.argv) != 4):
        print("Please eneter correct arguments")
        print("1 : Folder name")
        print("2 : Extension1")
        print("3 : Extension2")
        return
    
    else:        
        schedule.every(30).seconds.do(DirectoryRename, sys.argv[1],sys.argv[2], sys.argv[3])

        while(True):
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()