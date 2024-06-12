import sys
args=sys.argv

path1="/media/chinourobot/HDCZ-UT/takayama/kmeans/result/test-set-one.txt"
xxx=-1
list1=[]
with open(path1,"r") as f1:
 for i1 in f1:
  if xxx <= i1.split()[1]:
   list1.append(i1.split())
  else:
   path2="/media/chinourobot/HDCZ-UT/takayama/kmeans/result/%s-result/%s" % (args[1],args[2])
   min_1=0
   num=0
   num_mul=0
   multiplier=0
   with open(path2,"r") as f2:
    for i2 in f2:
     path3="%s/%s.txt" % (sys.argv[3],'{0:03d}'.format(int(i2.split()[1])))
     with open(path3,"r") as f3:
      for i3 in f3:
       aaa=0
       for i4 in list1:
        if int(i4[1])==int(i3.split()[0]):
         min_1=float(i3.split()[1])
         multiplier=float(i2.split()[0])
         aaa=1
         break
       if aaa==1:
        break
     num+=min_1*multiplier
   path4="%s/%s" % (args[4],args[2])
   with open(path4,"a") as f4:
    f4.write(list1[0][2]+" "+str(num)+"\n")
   list1=[]
   list1.append(i1.split())
  xxx=i1.split()[1]

min_1=0
num=0
num_mul=0
multiplier=0
with open(path2,"r") as f5:
 for i5 in f5:
  path3="%s/%s.txt" % (sys.argv[3],'{0:03d}'.format(int(i5.split()[1])))
  with open(path3,"r") as f6:
   for i6 in f6:
    aaa=0
    for i7 in list1:
     if int(i7[1])==int(i6.split()[0]):
      min_1=float(i6.split()[1])
      multiplier=float(i5.split()[0])
      aaa=1
      break
    if aaa==1:
     break
  num+=min_1*multiplier
path4="%s/%s" % (args[4],args[2])
with open(path4,"a") as f7:
 f7.write(list1[0][2]+" "+str(num))











