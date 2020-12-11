import os
import glob
import shutil
import re

# THIS SCRIPT WILL COPY DATA FROM DIRECTORY C TO D
# If same name files are found it would be replaced

keywords=['aadhar','pan','ecard']

#File entries
entries = os.listdir('C:\\Users\\kunal\\Documents\\test')
#Current Directory
os.chdir("C:\\Users\\kunal\\Documents\\test")

#Grep all txt files from test folder
text_file = glob.glob('*.txt')
text_length = len(text_file)

#Print all text files
print(text_file)

#Save all keyword data to D:\\logs.txt
for i in range(text_length):
    with open(text_file[i], 'r') as fp:
        lines = fp.read().splitlines()
        c = 0
        for l in lines:
            for ja in keywords:
                if ja in l:
                    f = open("D:\\logs.txt", "a")
                    f.write(l + '\n')
                    f.close()

#Grep all jpg files
image_file = glob.glob('*.jpg')
image_length = len(image_file)

#print all images
print(image_file)

#Copy all jpg images to D:\\*
for i in range(image_length):
    shutil.copy2(image_file[i], 'D:\\'+str(image_file[i]))


#Recursing the search into subdirectories

for root, dirs, files in os.walk('C:\\Users\\kunal\\Documents\\test\\'):
    directories = len(dirs)
    for i in range(directories):
        print(dirs[i])
        entries = os.listdir('C:\\Users\\kunal\\Documents\\test\\' + str(dirs[i]))
        os.chdir("C:\\Users\\kunal\\Documents\\test\\" + str(dirs[i]))

        # Grep all txt files from test folder
        text_file = glob.glob('*.txt')
        text_length = len(text_file)

        # Print all text files
        print(text_file)

        # Save all keyword data to D:\\logs.txt
        for i in range(text_length):
            with open(text_file[i], 'r') as fp:
                lines = fp.read().splitlines()
                c = 0
                for l in lines:
                    for ja in keywords:
                        if ja in l:
                            f = open("D:\\logs.txt", "a")
                            f.write(l + '\n')
                            f.close()

        # Grab all jpg files
        image_file = glob.glob('*.jpg')
        image_length = len(image_file)

        # print all images list
        print(image_file)

        # Copy all jpg images to D:\\*
        for i in range(image_length):
            shutil.copy2(image_file[i], 'D:\\' + str(image_file[i]))
