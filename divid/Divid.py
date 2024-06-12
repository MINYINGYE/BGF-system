import os
import numpy as np
import sys
import glob
import shutil
import time
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

# def copyfile(pathtxt, read_path , save_path):
# 	path = np.loadtxt(pathtxt,dtype=str)
# 	# print(path)
# 	for ind, value in enumerate(tqdm(path)):
# 		filename = os.path.splitext(os.path.basename(value[0]))[0]
# 		path = os.path.join(read_path + '/' + filename + '.png')
# 		savepath = os.path.join(save_path + '/' + value[1] + '/' + filename + '.png')
# 		if not os.path.exists(os.path.join(save_path + '/' + value[1])):
# 			os.makedirs(os.path.join(save_path + '/' + value[1]))
# 		print(path)
# 		print(savepath)
# 		shutil.copyfile(path,savepath)

if __name__ == '__main__':
	args = sys.argv
	path1 = args[1]
	path2 = args[2]
	pathtxt = args[3]

	if not os.path.exists(path2):
		os.makedirs(path2)
	namelist = np.loadtxt(pathtxt, dtype=str)
	# executor = ThreadPoolExecutor(max_workers=3)
	for value in tqdm(namelist):
		filename = os.path.splitext(os.path.basename(value[0]))[0]
		path = os.path.join(path1 + '/' + filename + '.png')
		savepath = os.path.join(path2 + '/' + value[1] + '/' + filename + '.png')
		if not os.path.exists(os.path.join(path2 + '/' + value[1])):
			os.makedirs(os.path.join(path2 + '/' + value[1]))
		#         print(path)
		#         print(savepath)

		shutil.copyfile(path, savepath)

		# executor.submit(shutil.copyfile, path, savepath)
