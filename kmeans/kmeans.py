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
#data1 = data[~np.isnan(data).any(axis=1)]
#print ("delete nan")

fname = args[2]
#学習するなら
#try:

if "yes" == args[6]:
	cls = KMeans(n_clusters=10, n_jobs=5)
	print ("learning completed")
	pred = cls.fit_predict(data)
	joblib.dump(cls, fname)

#except:
	#with open('test.txt', 'a') as f:
	#	f.write(sys.exc_info())
	#print aaaaaaaaaaaaaaa
#学習済みなら
if "no" == args[6]:
	cls = joblib.load(fname)
	print ("load model")
	pred = cls.fit_predict(data)

print ("predict completed")
np.savetxt(args[3], pred, fmt = '%.f')


for i in range(10):
	a = np.mean(data[pred==i], axis=0),
	with open(args[4], 'a') as f_handle:
		np.savetxt(f_handle, a, fmt = '%.7f')
	
	bbb = data[pred==i]
	with open('%s%s-des.txt' %(args[5], i) ,'wb') as handle:
		np.savetxt(handle,bbb , fmt = '%.7f')

