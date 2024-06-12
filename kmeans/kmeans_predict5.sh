start_time=`date +%s`

path1=/media/chinourobot/HDCZ-UT/takayama/ziken/feature/$1
path2=zisyo/joblib_1
out_dir=result/$1-result
rm -r $out_dir
mkdir -p $out_dir

python2 kmeans_predict5.py $path2/cluster.joblib $1 $out_dir

end_time=`date +%s`
time=$((end_time - start_time))
echo $time















