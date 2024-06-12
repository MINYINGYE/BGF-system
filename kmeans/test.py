import numpy as np
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import sys


data = np.loadtxt("/media/chinourobot/HDCZ-UT/takayama/kmeans/process/result/100/cluster-0.txt")
#data2 = np.loadtxt("/media/chinourobot/HDCZ-UT/takayama/kmeans/process/result/100/cluster-0.txt")

for i in range(10):
 if len(data)!=0:
  print(i)
