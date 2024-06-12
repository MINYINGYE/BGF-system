# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 21:35:24 2018
@author: 13260
"""
import os
from keras.applications.vgg19 import VGG19
from keras.preprocessing import image
from keras.applications.vgg19 import preprocess_input
from keras.models import Model
import numpy as np
import shutil
from tqdm import tqdm
import time
import sys
 
 
 
 
def feature_extraction(filename,save_path):
    model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc2').output)
    img_path = filename 
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    fc2 = model.predict(x)     ## 获取VGG19全连接层特征
    #print(fc2.shape)
    save_path='%s.txt'%(save_path)
    #print(save_path)
    np.savetxt(save_path,fc2,fmt='%s') ## 保存特征文件
    
def read_image(rootdir,save_path):
    list = os.listdir(rootdir) #列出文件夹下所有的目录与文件
    #print(list)
    files = []
    
    pbar = tqdm(total = len(range(0,len(list))))
    for i in range(0,len(list)):
       path = os.path.join(rootdir,list[i])
       save = os.path.join(save_path,list[i])
       #print(path)
       #print(save)
       dirs = os.listdir(path)
       
       for file in dirs:
         savePath1 = os.path.join(save,file)
         if not os.path.exists(savePath1):
                 os.makedirs(savePath1)
         #print(savePath1)
         filename1 = os.path.join(path,file)
         #print(filename1)
         nums = os.listdir(filename1)
         for j in nums:
            savePath = os.path.join(savePath1,j[:-4])
            filename = os.path.join(filename1,j)
            #print(savePath)
            #print(filename)
            feature_extraction(filename,savePath)
            #print("successfully saved "+ file[:-4] +".txt !")
     
       print(i)
       pbar.update(1)
    pbar.close
if __name__ == '__main__':
    base_model = VGG19(weights='imagenet', include_top=True) ##加载VGG19模型及参数
    #print("Model has been onload !")
    rootdir = '../0108sapatchimg/png_0108sa'  ##图片路径
    save_path = "../0108safg"   ##提取特征文件保存路径
    shutil.rmtree(save_path)
    os.makedirs(save_path)
    read_image(rootdir,save_path)
    #print("work has been done !")
