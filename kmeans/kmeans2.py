#!/usr/bin/python
#-*- coding: utf-8 -*-
#import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import sys


args = sys.argv
data = np.loadtxt(args[1])
print ('load %s' %args[1])


fname = args[2]
#学習するなら
#try:

cls = KMeans(n_clusters=1000, n_jobs=-1)
print ("learning completed")
pred = cls.fit_predict(data)
joblib.dump(cls, fname)


a=0
for i in range(1000):
 print(i)
 a='{0:03d}'.format(i)
 bbb = data[pred==i]
 with open('%s%s.txt' %(args[3], a) ,'wb') as handle:
  np.savetxt(handle,bbb , fmt = '%.7f')

