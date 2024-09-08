import os

directory = '/'   #it will show files of the root folder of this package

contents = os.listdir(directory)

for i in contents:
    print(i)