import os
import datetime

date = datetime.datetime.today().strftime("%Y%m%d_%H%M%S")
print('mkdir: ', date)
os.mkdir(date)