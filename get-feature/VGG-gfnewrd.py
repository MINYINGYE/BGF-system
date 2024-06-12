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
import sys
from tqdm import tqdm
import glob
 
 
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
    # print('in',save_path)
    np.savetxt(save_path,fc2,fmt='%s') ## 保存特征文件
            
if __name__ == '__main__':
    base_model = VGG19(weights='imagenet', include_top=True) ##加载VGG19模型及参数
    #print("Model has been onload !")
    dir_path  = sys.argv[1]  ##图片路径
    savepath = sys.argv[2]   ##提取特征文件保存路径
    print(savepath)
    if not os.path.exists(savepath):
        os.makedirs(savepath)
    for rootdir in tqdm(glob.glob(dir_path + "/*")):
        save_path = os.path.join(savepath + "/"+ os.path.splitext(rootdir.split('/',6)[6])[0])
        feature_extraction(rootdir,save_path)
    #print("work has been done !")
