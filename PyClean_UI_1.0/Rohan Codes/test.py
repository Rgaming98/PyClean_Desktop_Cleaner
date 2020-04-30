# import win32api,os

# drives = win32api.GetLogicalDriveStrings()
# drives = drives.split('\000')[:-1]
# # print(os.walk(drives[0]))
# # for i,j,k in os.walk(drives[1]): 
# #     print(j)
# print(os.listdir(drives[1]))

import os
linkdic = {
    "newpath" : ''
}

linkdic["newpath"] = str(input("Enter a path "))

def sizecalculator():
    total_size = 0
    lookingzone = linkdic["newpath"]  #modulating path to be added. 
    for path, dirs, files in os.walk(lookingzone):
        for f in files:
            fp = os.path.join(path, f)
            total_size += os.path.getsize(fp)
    print("Directory size: " + str(total_size/1073741824)[:5]+" GB")

if __name__ == "__main__":
    sizecalculator()
