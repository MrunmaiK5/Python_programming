import schedule
import os
import sys
import time
import shutil
import hashlib

########################################################################################################
#   Function name   :   DirectoryChecksum
#   Description     :   Find checksum of all files of given directory
#   Input           :   String
#   Output          :   Nothing
#   Author          :   Mrunmai Jitendra Khadpe
#   Date            :   24/02/26
########################################################################################################

def DirectoryChecksum(DictName):
    try:
        FolderName = "D32_1"
        Ret = os.path.exists(FolderName)

        if(Ret == True):
            Ret = os.path.isdir(FolderName)
            if(Ret == False):
                print("Unable to create folder")
                return
        else:
            os.mkdir(FolderName)
            print("Directory for log files gets created succesfully")
        
        name = time.strftime("%Y-%m-%d_%H_%M_%S")+".log"
        FileName = os.path.join(FolderName,"Mrunmai_%s" %name)
        lobj = open(FileName,"w")

        if (os.path.exists(DictName) == False):
            print("Unable to calculate checksum as no such directory exists")
            return
        
        if (os.path.isdir(DictName) == False):
            print("Invalid folder name")
            return

        for root, subdir, files in os.walk(DictName):

            for file in files:
                file = os.path.join(root,file)
                fobj = open(file,"rb")

                hobj = hashlib.md5()
                Buffer = fobj.read()
                fobj.close()
                hobj.update(Buffer)

                chk = hobj.hexdigest()

                lobj.write("File name :"+file+" CheckSum : "+chk+"\n") 

        
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

        schedule.every(20).seconds.do(DirectoryChecksum, sys.argv[1])
        print("Process has been started")
        while(True):
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    main()