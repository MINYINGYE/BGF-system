#!/usr/bin/python
#-*- coding: utf-8 -*-
#import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import sys

args = sys.argv
data = np.loadtxt(args[1])

#print ('load %s' %args[1])
#data1 = data[~np.isnan(data).any(axis=1)]
#print ("delete nan")

fname = args[2]
#学習するなら
#try:

if "yes" == args[5]:
	cls = KMeans(n_clusters=10, n_jobs=-1)
#	print ("learning completed")
	pred = cls.fit_predict(data)
	joblib.dump(cls, fname)

#except:
	#with open('test.txt', 'a') as f:
	#	f.write(sys.exc_info())
	#print aaaaaaaaaaaaaaa
#学習済みなら
if "no" == args[5]:
 cls = joblib.load(fname)
# print ("load model")
# print(len(data))
 if len(data)==512:
  pred = cls.predict([data])
 else:
  pred = cls.predict(data)#データが一つの５１２の場合はエラーを吐き、[n...n]から[512]のlistになるから

#print ("predict completed")
#np.savetxt(args[3], pred, fmt = '%.f')

if len(pred)==1:
 for i in range(10):
  if pred==i:
#   print(i)
   bbb = [data]
#   print(bbb)
   with open('%s%s-des.txt' %(args[4], i) ,'wb') as handle:
    np.savetxt(handle,bbb , fmt = '%.7f')
else:
 for i in range(10):
   if (pred==i).any() == True:
    bbb = data[pred==i]
    with open('%s%s-des.txt' %(args[4], i) ,'wb') as handle:
     np.savetxt(handle,bbb , fmt = '%.7f')














