import pandas as pd
import glob
import cv2
import os


path="./Train_Dev/old_csv/"
path_img="./Train_Dev/old_picture/"


# path="./Train_Dev/new_csv/"
# path_img="./Train_Dev/new_picture/"

# path="./Train_Dev/mid_csv/"
# path_img="./Train_Dev/mid_picture/"

# os.makedirs(path+'../train_608', exist_ok=True)
os.makedirs(path+'../other_608', exist_ok=True)

A = 608
B = 30

def alter(file,old_str,new_str):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
           if old_str in line:
                line = line.replace(old_str,new_str)
           file_data += line
    with open(file,"w",encoding="utf-8") as f:
       f.write(file_data)

for x in glob.glob(path+'*.csv'):
   
    data=pd.read_csv(x)
    print(os.path.splitext(os.path.basename(x))[0])
    img = cv2.imread(path_img+os.path.splitext(os.path.basename(x))[0]+".JPG")
    p_x=img.shape[1]
    p_y=img.shape[0]
    a=float(data.columns[0])
    b=float(data.columns[1])

    data.columns = ['x','y']
    data.loc[len(data.index)+1]=(a,b)
    data.info()

    o_x=int(p_x/A)
    o_y=int(p_y/A)
    
    for name in range(o_x*o_y):

        mask=(data["x"]>=A*(name%o_x)) & (data["x"]<A*(1+name%o_x)) & (data["y"]>=A*(name/o_x))&(data["y"]<A*(1+name/o_x))
    
        ans = pd.DataFrame()
        ans["class"]=0
        ans=ans.append(data[mask],ignore_index=True)
        
        ans["x"]=ans["x"]%A/A
        ans["y"]=ans["y"]%A/A
        
        
        ans["w"]=B/A
        ans["h"]=B/A
        
        ans["class"]=0
 
        
        ans.to_csv(path+'../other_608/' + os.path.splitext(os.path.basename(x))[0]+'_'+ str(name)+'.txt',index=False,header=False)
        alter(path+'../other_608/' + os.path.splitext(os.path.basename(x))[0]+'_'+ str(name)+'.txt',',',' ')
    
    
    