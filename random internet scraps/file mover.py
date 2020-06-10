import os
import shutil

path = r'C:\Users\PowerLogic\Documents'
names = os.listdir(path)
folder_name = ['word', 'browser html', 'photoshop', 'powerpoints']

for x in range(0,4):
    if not os.path.exists(path+folder_name[x]):
        os.makedirs(path+folder_name[x])

for files in names:
    if '.docx' in files and not os.path.exists(path+'word/'+files):
        shutil.move(path+files, path+'word/'+files)
    if '.html' in files and not os.path.exists(path+'browser html/'+files):
        shutil.move(path+files, path+'browser html/'+files)
    if '.psd' in files and not os.path.exists(path+'photoshop/'+files):
        shutil.move(path+files, path+'photoshop/'+files)
    if '.pptx' in files and not os.path.exists(path+'powerpoint/'+files):
        shutil.move(path+files, path+'powerpoint/'+files)
