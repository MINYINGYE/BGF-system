import sys

path1="%s/%s" % (sys.argv[1],sys.argv[2])
path2="%s/%s" % (sys.argv[3],sys.argv[4])
#print(path1)
min_1=0
num=0
#num_mul=0
with open(path1,"r") as f1:
 for i1 in f1:
  min_2=100
  print("a")
  with open(path2,"r") as f2:
   for i2 in f2:
#    print(int(i1.split()[0])*int(i2.split()[0]),i1.split()[1],i2.split()[1])
    path3="%s/%s.txt" % (sys.argv[5],'{0:03d}'.format(int(i1.split()[1])))
    with open(path3,"r") as f3:
     for i3 in f3:
      if i2.split()[1]==i3.split()[0]:
       min_1 = float(i3.split()[1])
    if min_2 >= min_1:
     min_2=min_1
     multiplier=int(i1.split()[0])
#  print(min_2)
  num+=min_2*multiplier
#  num_mul+=multiplier
path3="%s/%s" % (sys.argv[6],sys.argv[2])
print(path3)
with open(path3,"a") as f3:
 f3.write(sys.argv[4]+" "+str(num/500)+"\n")
#print(num/num_mul,num_mul)

#i2.split()[1]==i3.split()[1]

#    multiplier=int(i1.split()[0])
#    num_mul+=multiplier


"""
import sys
args=sys.argv


path1="/media/chinourobot/HDCZ-UT/takayama/kmeans/result/test-result-name.txt"      #"/media/chinourobot/HDCZ-UT/takayama/kmeans/result/2012-01-15-result-name.txt"
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
    with open(path3,"r") as f2:
     for i2 in f2:
      with open(path4,"r") as f3:
       for i3 in f3:
        if int(i3.split()[0])==int(i2.split()[1]):
         print(int(i2.split()[1]),int(i3.split()[0]))
         min_1=float(i3.split()[1])
         break
    num+=min_1
    multiplier=int(i1.split()[0])
    num_mul+=multiplier
  print(args[2],ix.split()[0],num,num_mul)
"""



