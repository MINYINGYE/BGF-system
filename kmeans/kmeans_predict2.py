#!/usr/bin/python
#-*- coding: utf-8 -*-
#import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import sys
import time

if __name__ == '__main__':
 start = time.time()

 args = sys.argv
 data = np.loadtxt(args[1])

#print ('load %s' %args[1])
#data1 = data[~np.isnan(data).any(axis=1)]
#print ("delete nan")

 fname = args[2]
#学習するなら
#try:


 cls = joblib.load(fname)
 if len(data)==512:
  pred = cls.predict([data])
 else:
  pred = cls.predict(data)#データが一つの５１２の場合はエラーを吐き、[n...n]から[512]のlistになるから

#print ("predict completed")

 if len(pred)==1:
  for i in range(10):
   if pred==i:
#   print(i)
    bbb = [data]
#   print(bbb)
    with open('%s%s' %(args[3], i) ,'wb') as handle:
     np.savetxt(handle,bbb , fmt = '%.7f')
 else:
  for i in range(10):
    if (pred==i).any() == True:
     bbb = data[pred==i]
     with open('%s%s' %(args[3], i) ,'wb') as handle:
      np.savetxt(handle,bbb , fmt = '%.7f')







 elapsed_time = time.time() - start
 print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")







