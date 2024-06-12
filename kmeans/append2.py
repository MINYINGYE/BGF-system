#!/usr/bin/python
#-*- coding: utf-8 -*-
#import pandas as pd
import numpy as np
import sys

args = sys.argv
aa=[]
data = np.loadtxt(args[1])
a = np.mean(data, axis=0)
#print(a)
with open(args[2], 'a') as f_handle:
 np.savetxt(f_handle,[a], fmt = '%.7f')


