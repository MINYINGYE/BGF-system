<<1aaa
in1=2012-01-15-all.txt

d1=$1/cluster_des_1
j0=$1/joblib_1


mkdir -p $d1
mkdir -p $r1
mkdir -p $j0


python2 kmeans2.py $in1 $j0/cluster.joblib $d1/
1aaa

#cluster代表の結合
rm -r $1/zisyo1000.txt
./append2.sh $1/cluster_des_1 $1/zisyo1000.txt










