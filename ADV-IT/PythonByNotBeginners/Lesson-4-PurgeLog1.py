#!/bin/python3
# -------------------------------------------------------
# Program by Zhuravlev D.D.
#
# Version       Date           Info
# 1.0           2022       Initial Version
# -------------------------------------------------------
import shutil
import os
import sys
# Сделали проверку на то, что пользователь ввел нужное колличество параметров для работы нашей функции
if(len(sys.argv) < 4):
    print("Missing argument")
    exit(1)
# Перечислели переменные которые будут принимать значения параметров перечисленных пользователем
filename = sys.argv[1]
limitsize = int(sys.argv[2])
lognumber = int(sys.argv[3])
#Проверяем при помощи библиотеки os(точнее ее функции (path.isfile)) есть ли вообще в системе такой файл
if(os.path.isfile(filename) == True):
    logfilesize = os.stat(filename).st_size
    logfilesize = logfilesize / 1024
    if(logfilesize >= limitsize):
        if(lognumber > 0):
            for currentFileNimber in range(lognumber, 1, -1):
                src = filename + "_" + str(currentFileNimber-1)
                dst = filename + "_" + str(currentFileNimber)
                if(os.path.isfile(src) == True):
                    shutil.copyfile(src, dst)
                    print("Copied: " + src + " to " + dst)
            shutil.copyfile(filename, filename + "_1")
            print("Copied: " + filename + " to " + filename + "_1")
        myfile = open(filename, 'w')
        myfile.close()
