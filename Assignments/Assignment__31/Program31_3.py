import schedule
import os
import sys
import time
import shutil

########################################################################################################
#   Function name   :   DirectoryCopy
#   Description     :   Copies all files from first directory to secind directory
#   Input           :   String, String
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   10/02/26
########################################################################################################

def DirectoryCopy(Dict1, Dict2):

    os.makedirs(Dict2,exist_ok=True)

    if (os.path.exists(Dict1) == True):
        if(os.path.isdir(Dict1) == True):
            for dir, subdir, files in os.walk(Dict1):
                for file in files:
                    src_path = os.path.join(dir,file)
                    relative = os.path.relpath(src_path,Dict1)
                    dest_path = os.path.join(Dict2,relative)

                    os.makedirs(os.path.dirname(dest_path),exist_ok=True)

                    shutil.copy2(src_path, dest_path)
            print("Successfully copies the files")

        else:
            print("Please enter correct folder name")

    else:
        print("The dirsctory does not exists")       


def main():
    print(len(sys.argv))
    if(len(sys.argv) != 3):
        print("Please eneter correct arguments")
        print("1 : Source folder name")
        print("2 : Destination folder name")
        return
    else:
        
        schedule.every(20).seconds.do(DirectoryCopy, sys.argv[1],sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()