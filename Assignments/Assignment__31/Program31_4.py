import schedule
import os
import sys
import time
import shutil

########################################################################################################
#   Function name   :   DirectoryCopyExt
#   Description     :   Copies files having given extension from first directory to secind directory
#   Input           :   String, String, String
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   10/02/26
########################################################################################################

def DirectoryCopyExt(Dict1, Dict2, Ext):

    os.makedirs(Dict2,exist_ok=True)

    if (os.path.exists(Dict1) == True):
        if(os.path.isdir(Dict1) == True):
            for dir, subdir, files in os.walk(Dict1):
                for file in files:
                    name = file.split('.')
                    if Ext == name[1]:
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
    if(len(sys.argv) != 4):
        print("Please eneter correct arguments")
        print("1 : Source folder name")
        print("2 : Destination folder name")
        print("3 : Extension")
        return
    else:
        
        schedule.every(20).seconds.do(DirectoryCopyExt, sys.argv[1],sys.argv[2], sys.argv[3])

        while(True):
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()