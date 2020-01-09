import os
import shutil

from_dir=input('ENTER the dir of folder to protect')
fname=input('Enter folder name to create')
pasw=input('Enter the password')

todir='C:/Users/hussainint/Desktop'
todir=os.path.join(todir,fname)
os.mkdir(todir)

for i in pasw:
    for j in range(1,11):
        path=os.path.join(todir,str(j))
        try:
            os.mkdir(path)
        except:
            print('error1')
        for k in range(1,11):
            path2=os.path.join(path,str(k))
            try:
                os.mkdir(path2)
            except:
                print('error2')
            
    todir=todir+'/'+i

try:
    shutil.move(from_dir,todir)
except:
    print()
    
