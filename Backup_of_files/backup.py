import os
import time

#List of reqired files
source = ['"C:\\My Documents"', 'C:\\Downloads']

target_dir = 'E:\\Backup' #Choose your path
#Name of subdir
today = target_dir + os.sep + time.strftime('%Y%m%d')
#Name of Zip files
now = time.strftime('%H%M%S')

#Your comment for Backup
comment = input("Enter your comment --> ")
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

#Mkdir
if not os.path.exists(today):
    os.mkdir(today)
    print('Directory created successfulyy', today)

#Zip
zip_command = "zip -qr {0} {1}".format(target, " ".join(source))

#Start
if os.system(zip_command) == 0:
    print('Backup has been successfulyy saved to the ', target)
else:
    print('Something went wrong. Backup failed')
