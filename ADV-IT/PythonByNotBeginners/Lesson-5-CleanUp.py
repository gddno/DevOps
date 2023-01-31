# -------------------------------------------------------
# Program by Zhuravlev D.D.
#
# Version       Date           Info
# 1.0           2022       Initial Version
# -------------------------------------------------------
import os, time

min = 1   #Maximal age of file to stay, older file will be deleted
folders = [
                "D:\DevOps\DevOps\PythonByNotBeginners\Musorka\Hlam",
                "D:\DevOps\DevOps\PythonByNotBeginners\Musorka\Musor",
                "D:\DevOps\DevOps\PythonByNotBeginners\Musorka\Raznoe"
]
total_deleted_size = 0   #Bytes
total_deleted_file = 0
total_deleted_directory = 0

now_time = time.time() # Get current Time in Second
age_time = now_time - 60*min

def delete_old_files(folder):
    global total_deleted_file
    global total_deleted_size
    for path, dirs, files in os.walk(folder):
        for file in files:
            fileName = os.path.join(path, file)
            fileTime = os.path.getmtime(fileName)
            if fileTime < age_time:
                sizeFile = os.path.getsize(fileName)
                total_deleted_size += sizeFile
                total_deleted_file += 1
                print("deleting file: " + str(fileName))
                os.remove(fileName)

def delete_empty_dir(folder):
    global total_deleted_directory
    empty_folders_in_this_run = 0
    for path, dirs, files in os.walk(folder):
        if (not dirs) and (not files):
            total_deleted_directory += 1
            empty_folders_in_this_run+= 1
            print("Deleting empty Dir :" + str(path))
            os.rmdir(path)
        if empty_folders_in_this_run > 0:
            delete_empty_dir(folder)
#=======================MAIN===============================================
start_time = time.asctime()

for folder in folders:
    delete_old_files(folder)        #delete old files
    delete_empty_dir(folder)        #delete empty folders

finish_time = time.asctime()

print("---------------------------------------------------------------------")
print("Start time: "                    + str(start_time))
print("Total Deleted Size: "            + str(total_deleted_size/1024/1024) + "MB")
print("Total Deleted Files: "           + str(total_deleted_file))
print("Total Deleted Empty Folders: "   + str(total_deleted_directory))
print("Finish Time: "                   + str(finish_time))
print("-------------------EOF-----------------------------------------------")
