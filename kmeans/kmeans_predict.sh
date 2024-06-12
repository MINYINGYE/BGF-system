start_time=`date +%s`
j0=zisyo/joblib/1
j1=zisyo/joblib/10
j2=zisyo/joblib/100
#in2=../../3d-10des.txt
#o=delete_nan1.txt
input_dir=/media/chinourobot/HDCZ-UT/takayama/ziken/feature/$1 #
output_dir=result/$1-result
rm -r $output_dir
mkdir -p $output_dir
count1=0
for i in `ls $input_dir`
do
    count1=$((count1+1))
    echo "##############################" $count1
    in1=$input_dir/$i
    #学習ならばyes、学習済みならばno
#    rm -r process/cluster
#    mkdir process/cluster
#    c1=process/cluster/10
#   c2=process/cluster/100
 #   c3=process/cluster/1000

    rm -r process/cluster_des
    mkdir process/cluster_des
    d1=process/cluster_des/10
    d2=process/cluster_des/100
    d3=process/cluster_des/1000

    rm -r process/cls_num #kesu
    mkdir process/cls_num
    r1=process/cls_num/10
    r2=process/cls_num/100
    r3=process/cls_num/1000


    mkdir -p $d1 $d2 $d3
    mkdir -p $r1 $r2 $r3


    #python2 kmeans.py $in2 $j/$n0/$c.$j $r/$n1/$c.txt $c/$n1/$c.txt $d/$n1/$c- yes
#echo learn

    #python2 delete_nan.py $in1 $o

    python2 kmeans_predict.py $in1 $j0/cluster.joblib $r1/cluster.txt $d1/cluster- no
    echo 10

    ls $d1| sed -e 's/-des.txt//g' | while read l
    do
	python2 kmeans_predict.py $d1/$l-des.txt $j1/$l.joblib $r2/$l.txt $d2/$l no
    done
    echo 100

    ls $d2| sed -e 's/-des.txt//g' | while read l2
    do
	python2 kmeans_predict.py $d2/$l2-des.txt $j2/$l2.joblib $r3/$l2.txt $d3/$l2 no
    done
#    echo 1000

    wc -l $d3/* | sed "s/process\/cluster_des\/1000\/cluster-//g" | sed "s/-des.txt//g" | sed "/    500 合計/d" | sed 's/^[ \t]*//g' > $i

    mv $i $output_dir
done






end_time=`date +%s`
time=$((end_time - start_time))
echo $time




#行頭の空白削除
#sed 's/^[ \t]*//'

#行末の空白削除
#sed -e 's/[ \t]*$//'











