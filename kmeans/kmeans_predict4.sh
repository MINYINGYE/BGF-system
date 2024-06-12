start_time=`date +%s`

path1=/media/chinourobot/HDCZ-UT/takayama/ziken/feature/$1
path2=zisyo/joblib_1
out_dir=result/$1-result
rm -r $out_dir
mkdir -p $out_dir
count1=0
for i in `ls $path1`
do
count1=$((count1+1))
echo $count1
python2 kmeans_predict4.py $path1/$i $path2/cluster.joblib $out_dir/ $i
done



end_time=`date +%s`
time=$((end_time - start_time))
echo $time















