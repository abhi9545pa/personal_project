import os
import shutil

# get the path of current working direc..
path = os.getcwd()[:os.getcwd().rfind('\\')]
#path = os.getcwd()

for file in os.listdir(path):
    name , exten = os.path.splitext(file)
    #print(f'{name},{exten}')
    if len(exten) > 0 : # for all the files but not the folders
        if os.path.exists(path+"\\"+exten):
            shutil.move(path+'\\'+file,path+'\\'+exten+'\\'+file)
        else:
            os.makedirs(path+'\\'+exten)
            shutil.move(path+'\\'+file,path+'\\'+exten+'\\'+file)