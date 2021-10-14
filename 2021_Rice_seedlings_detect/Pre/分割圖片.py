# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 19:21:00 2021

@author: ACER-20
"""
import cv2
import math
import glob
import os


# path="./Train_Dev/old_picture/" #這是相對路徑，用相對路徑來選取分割圖片的檔案
path="./Train_Dev/new_picture/"

w=607
h=607

os.makedirs(path+'../train_608', exist_ok=True)

#test = cv2.imread(name)
#cv2.imshow("test", test)  #圖片顯示
#cv2.waitKey(0)
for i in glob.glob(path+'*.JPG'):
    img = cv2.imread(i)
    hight = img.shape[1]        #求圖片x軸畫質
    width = img.shape[0]        #求圖片y軸畫質 
    hight=math.floor(hight/(h+1)) #算以224能分成幾塊
    width=math.floor(width/(w+1))
    al=hight*width
    for n in range(al):
        n_str=str(n)
        x=(n%hight)*(w+1)        #利用編號定位出要分割的x和y的位置
        g=math.floor(n/hight)
        y=(g)*(h+1)
        
        crop_img = img[y:y+h, x:x+w]#分割圖片
        cv2.imwrite(path+'../train_608/'+os.path.splitext(os.path.basename(i))[0]+'_'+n_str+'.jpg', crop_img)
        