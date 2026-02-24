import schedule
import os
import sys
import time
import shutil
import hashlib

########################################################################################################
#   Function name   :   DirectoryDuplicate
#   Description     :   Writes all duplicate file names into a file "Log.txt"
#   Input           :   String
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   11/02/26
########################################################################################################

def DirectoryDuplicate(DictName):
    try:        
        name = "Log.txt"
        lobj = open(name,"w")

        if (os.path.exists(DictName) == False):
            print("Unable to calculate checksum as no such directory exists")
            return
        
        if (os.path.isdir(DictName) == False):
            print("Invalid folder name")
            return

        duplicate = {}

        for root, subdir, files in os.walk(DictName):

            for file in files:
                Path = os.path.join(root,file)
                fobj = open(Path,"rb")

                hobj = hashlib.md5()
                Buffer = fobj.read()
                fobj.close()
                hobj.update(Buffer)

                chk = hobj.hexdigest()

                if chk in duplicate:
                    duplicate[chk].append(file)
                else:
                    duplicate[chk] = [file]

        Res = list(filter(lambda x : len(x) > 1 , duplicate.values()))
        
        for List in Res:
            for dpfile in List: 
                lobj.write(dpfile+"\n")

        lobj.close()

        print("Created log file successfully")
                 
    except:
        print("Unable to create log file")

def main():

    # python filename.py directory_name

    if (len(sys.argv) != 2):
        print("Please enter correct arguments")
        print("Enter folder name")

    else:

        schedule.every(20).seconds.do(DirectoryDuplicate, sys.argv[1])
        print("Process has been started")
        while(True):
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()