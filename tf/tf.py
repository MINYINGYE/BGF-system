import os
import random
import shutil
import sys
import glob
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor

path1="%s" % sys.argv[1]
path2="%s" % sys.argv[2]


def movefile(fileDir):
    pathDir = os.listdir(fileDir)
    filenumber = len(pathDir)
    # if filenumber > 1 :
    picknumber = 1
    sample = random.sample(pathDir, picknumber)
    # print(sample)
    for name in sample:
        shutil.copyfile(os.path.join(fileDir, name), os.path.join(tarDir, name))
    # else:
    #   shutil.copyfile(os.path.join(fileDir,name),os.path.join(tarDir,name))
    return


if __name__ == '__main__':
    # executor = ThreadPoolExecutor(max_workers=3)
    for f in tqdm(glob.glob(path1 + "/*")):
        # for f1 in sorted(glob.glob(f + "/*")):
        s = f.split('/', 5)[5]
        # print(f)
        # print(s)
        tarDir = os.path.join(path2, s)
        if not os.path.exists(tarDir):
            os.makedirs(tarDir)
        # print(tarDir)
        movefile(f)
