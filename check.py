import os
import shutil
source = input("entersourcefolder")
dest = input("enterdestfolder")
source = source + "/"
dest = dest + "/"
listoffiles = os.listdir(source)
for file in listoffiles:
    shutil.move((source + file),dest)