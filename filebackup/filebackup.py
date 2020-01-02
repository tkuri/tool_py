import os
import shutil
import glob
import datetime

datedir = datetime.datetime.today().strftime("%Y%m%d_%H%M%S")
print('mkdir: ', datedir)
os.mkdir(datedir)

# Specify backup file pattern
filelist = glob.glob('*.pth')
filelist += glob.glob('*.pdf')
filelist += glob.glob('*test*')

print(filelist)

for f in filelist:
    shutil.move(f, datedir)