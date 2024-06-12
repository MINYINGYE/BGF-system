#!/usr/bin/python
#-*- coding: utf-8 -*-
#import pandas as pd
import numpy as np
import sys

args = sys.argv
data = np.loadtxt(args[1])
print ('load %s' %args[1])

with open(args[2], 'a') as f_handle:
	np.savetxt(f_handle, data, fmt = '%.7f')


