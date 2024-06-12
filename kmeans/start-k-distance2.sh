start_time=`date +%s`


path1=/media/chinourobot/HDCZ-UT/takayama/kmeans/result/$1-result #query
path2=/media/chinourobot/HDCZ-UT/takayama/kmeans/zisyo_result/zisyo1000-2
path3=/media/chinourobot/HDCZ-UT/takayama/kmeans/distance/2012-01-08

count1=0
rm $path3/*
ls $path1 | while read line
do
count1=$((count1+1))
echo "##############"$count1
python k-distance2.py $1 $line $path2 $path3
done

end_time=`date +%s`
time=$((end_time - start_time))
echo "time" $time










