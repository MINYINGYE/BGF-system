#c=cluster
#o=app-cluster.txt

ls $1/10000 | while read l
do
python2 append.py $1/10000/$l $2
done
