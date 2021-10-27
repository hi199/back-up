import os
import shutil
source=input("source:")
destination=input("destination")
source=source+'/'
destination=destination+'/'
listofiles=os.listdir(source)
for file in listofiles:
    shutil.copy((source+file),destination)