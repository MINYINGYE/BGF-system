start_time=`date +%s`
j0=zisyo/joblib/1
j1=zisyo/joblib/10
j2=zisyo/joblib/100


input_dir=/media/chinourobot/HDCZ-UT/takayama/kmeans/$1    #/media/chinourobot/HDCZ-UT/takayama/ziken/feature/$1 
output_dir=result/$1-result
rm -r $output_dir
mkdir -p $output_dir
count1=0
for i in `ls $input_dir`
do
    count1=$((count1+1))
    echo "##############################" $count1
    in1=$input_dir/$i

    rm -r process/cluster_des2
    mkdir process/cluster_des2
    d1=process/cluster_des2/10
    d2=process/cluster_des2/100



    mkdir -p $d1 $d2

    echo $d1
    python2 kmeans_predict2.py $in1 $j0/cluster.joblib $d1/
    echo 10

    ls $d1 | while read l
    do
	python2 kmeans_predict2.py $d1/$l $j1/cluster-$l.joblib $d2/$l
    done
    echo 100

    ls $d2 | while read l2
    do
	python2 kmeans_predict3.py $d2/$l2 $j2/cluster-$l2.joblib $i $l2
    done

done






end_time=`date +%s`
time=$((end_time - start_time))
echo $time




#行頭の空白削除
#sed 's/^[ \t]*//'

#行末の空白削除
#sed -e 's/[ \t]*$//'











