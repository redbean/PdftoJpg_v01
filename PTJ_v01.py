#! /usr/bin/python
#

import os

path = input("Enter the path of pdf: ")
print path
files = os.listdir(path)


for i in files:
        if i[-3:] == "pdf":
                os.system("convert %s\%s[0] %s\%s.jpg" % (path, i,path, i[:-4]))


