#!/usr/bin/python
#-*- coding: utf-8 -*-
#import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import sys

args = sys.argv
data = np.loadtxt(args[1])

path1="/media/chinourobot/HDCZ-UT/takayama/kmeans/result/test-result/%s" % args[3]



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
pred=sorted(pred)
#print(pred)
abc=[]
aaa=11
count1=1
count2=-1

for i1 in pred:
 count2+=1
 if int(i1)!=aaa:
  count1=1
  abc.append(str(count1)+" "+args[4]+str(i1))
  aaa=int(i1)
 else:
  abc.remove(str(count1)+" "+args[4]+str(pred[count2]))
  count1+=1
  abc.append(str(count1)+" "+args[4]+str(i1)) 

with open(path1,"a") as f1:
 for i2 in abc:
  f1.write(i2.split()[0]+" "+i2.split()[1]+"\n")






