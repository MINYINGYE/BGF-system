start_time=`date +%s`


path1=/media/chinourobot/HDCZ-UT/takayama/kmeans/result/test-result #query
path2=/media/chinourobot/HDCZ-UT/takayama/kmeans/result/2 #database
path3=/media/chinourobot/HDCZ-UT/takayama/kmeans/zisyo_result/zisyo1000/zisyo1000name.txt
path4=/media/chinourobot/HDCZ-UT/takayama/kmeans/distance/2012-01-08
rm $path4/*
ls $path1 | while read line
do
ls $path2 | while read line2
do
python k-distance.py $path1 $line $path2 $line2 $path3 $path4
done
done

end_time=`date +%s`
time=$((end_time - start_time))
echo $time










