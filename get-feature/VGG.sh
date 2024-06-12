
rm -rf ../$2
mkdir ../$2

#ls $1 > doclist1.txt
count1=0
for line in $(ls $1)
do
 
 count1=$(($count1+1))
 dirname=../$2/$line/
  #echo "the dir name is $dirname"
  if [ ! -d $dirname  ];then
    mkdir $dirname
  #else
    #echo dir existS
  fi
 #ls $1/$line > filelist.txt
 count2=0
 for line2 in $(ls $1/$line)
 do
  count2=$(($count2+1))
  dirname2=../$2/$line/$line2
    #echo "the dir name is $dirname2"
    if [ ! -d $dirname2  ];then
      mkdir $dirname2
    #else
      #echo dir exist
    fi
   ls $1/$line/$line2 > pnglist.txt
   count3=0
   sed "s/.png//g" pnglist.txt > doclist3.txt
   for line3 in $(cat doclist3.txt)
   do
    count3=$(($count3+1))
    dirname3=../$2/$line/$line2/
    #echo "the dir name is $dirname3"
    if [ ! -d $dirname3  ];then
      mkdir $dirname3
    #else
      #echo dir exist
    fi
    startTime=`date +%Y%m%d-%H:%M`
    startTime_s=`date +%s`
    python3.7 VGG-gfnew.py $1/$line/$line2/$line3 ../$2/$line/$line2/$line3
    endTime=`date +%Y%m%d-%H:%M`
    endTime_s=`date +%s`
    sumTime=$[$endTime_s - $startTime_s]
    echo "$startTime ---> $endTime" "Totl:$sumTime seconds" 
   done
 done
done
