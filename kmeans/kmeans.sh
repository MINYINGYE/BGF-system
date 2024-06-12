in1=2012-01-15-all.txt
#in2=../../3d-10des.txt
#o=delete_nan1.txt
c1=$1/cluster/10
c2=$1/cluster/100
c3=$1/cluster/1000

d1=$1/cluster_des/10
d2=$1/cluster_des/100
d3=$1/cluster_des/1000

r1=$1/result/10
r2=$1/result/100
r3=$1/result/1000

j0=$1/joblib/1
j1=$1/joblib/10
j2=$1/joblib/100

#学習ならばyes、学習済みならばno

rm -rf $1/cluster
mkdir -p $c1 $c2 $c3
mkdir -p $d1 $d2 $d3
mkdir -p $r1 $r2 $r3
mkdir -p $j0 $j1 $j2

#python2 kmeans.py $in2 $j/$n0/$c.$j $r/$n1/$c.txt $c/$n1/$c.txt $d/$n1/$c- yes
#echo learn

#python2 delete_nan.py $in1 $o

python2 kmeans.py $in1 $j0/cluster.joblib $r1/cluster.txt $c1/cluster.txt $d1/cluster- yes
echo 10

ls $d1| sed -e 's/-des.txt//g' | while read l
do
python2 kmeans.py $d1/$l-des.txt $j1/$l.joblib $r2/$l.txt $c2/$l.txt $d2/$l yes
done
echo 100

ls $d2| sed -e 's/-des.txt//g' | while read l
do
python2 kmeans.py $d2/$l-des.txt $j2/$l.joblib $r3/$l.txt $c3/$l.txt $d3/$l yes
done
echo 1000

#cluster代表の結合
./append.sh $1/cluster $1/ap-cluster.txt










