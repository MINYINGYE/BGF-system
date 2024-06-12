import sys
args=sys.argv


path1="/media/chinourobot/HDCZ-UT/takayama/kmeans/result/test-result-name.txt"
#print(path1)

with open(path1,"r") as fx:
 for ix in fx:
  path2="/media/chinourobot/HDCZ-UT/takayama/kmeans/result/%s-result/%s" % (args[1],args[2])
  path3="/media/chinourobot/HDCZ-UT/takayama/kmeans/result/test-result/%s" % ix.split()[0]
  min_1=0
  num=0
  num_mul=0
  multiplier=0
  with open(path2,"r") as f1:
   for i1 in f1:
    path4="%s/%s.txt" % (sys.argv[3],'{0:03d}'.format(int(i1.split()[1])))
    with open(path4,"r") as f2:
     for i2 in f2:
      aaa=0
      with open(path3,"r") as f3:
       for i3 in f3:
        if int(i2.split()[0])==int(i3.split()[1]):
         min_1=float(i2.split()[1])
         aaa=1
         break
      if aaa==1:
       break
    num+=min_1
  path5="%s/%s" % (args[4],args[2])
  with open(path5,"a") as f4:
   f4.write(str(ix.split()[0])+" "+str(num)+"\n")




