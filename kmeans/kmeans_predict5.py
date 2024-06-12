#!/usr/bin/python
#-*- coding: utf-8 -*-
#import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import sys

args = sys.argv


path1="/media/chinourobot/HDCZ-UT/takayama/ziken/feature/2012-01-08-100-name.txt"


fname = args[1]



cls = joblib.load(fname)
with open(path1,"r") as fx:
 for ix in fx:
  path2="/media/chinourobot/HDCZ-UT/takayama/ziken/feature/%s/%s" % (args[2],ix.split()[0])
  path3="/media/chinourobot/HDCZ-UT/takayama/kmeans/%s/%s" % (args[3],ix.split()[0])
  data = np.loadtxt(path2)


  pred = cls.predict(data)
  pred=sorted(pred)

  abc=[]
  aaa=1001
  count1=1
  count2=-1

  for i1 in pred:
   count2+=1
   if int(i1)!=aaa:
    count1=1
    abc.append(str(count1)+" "+str('{0:03d}'.format(i1)))
    aaa=int(i1)
   else:
    abc.remove(str(count1)+" "+str('{0:03d}'.format(pred[count2])))
    count1+=1
    abc.append(str(count1)+" "+str('{0:03d}'.format(i1))) 

  with open(path3,"a") as f1:
   for i2 in abc:
    f1.write(i2.split()[0]+" "+i2.split()[1]+"\n")






