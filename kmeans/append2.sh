#c=cluster
#o=app-cluster.txt

ls $1 | while read l
do
python append2.py $1/$l $2
done
