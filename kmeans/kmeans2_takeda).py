#!/usr/bin/python
#-*- coding: utf-8 -*-
#import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import sys
import glob
import os

args = sys.argv

dir_path = args[1]

data_list = []
image_name_list = []

for f in sorted(glob.glob(dir_path + "/*")):
  for f1 in sorted(glob.glob(f + "/*")):
    for f2 in sorted(glob.glob(f1 + "/*")):
      data_vector = np.loadtxt(f2)
      data_list.append(data_vector)
      image_name_list.append(f2)
	
print(data_list)
data_matrix = np.array(data_list)
print(data_matrix)
np.savetxt('a1.txt',data_list)
#print ('load %s' %args[1])





fname = args[2]
#学習するなら
#try:

cls = KMeans(n_clusters=2000, n_jobs=-1)
print ("learning completed")
pred = cls.fit_predict(data_matrix)
#joblib.dump(cls, fname)
#np.savetxt(fname,pred)

new_data_array = np.vstack([np.array(image_name_list),pred])
print(new_data_array.T)

np.savetxt(fname,new_data_array.T,fmt = "%s")

"""
a=0
for i in range(1000):
 print(i)
 a='{0:03d}'.format(i)
 bbb = data[pred==i]
 with open('%s%s.txt' %(args[3], a) ,'wb') as handle:
  np.savetxt(handle,bbb , fmt = '%.7f')
"""
