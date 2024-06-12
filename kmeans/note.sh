/media/chinourobot/HDCZ-UT/takayama/kmeans
1  ./kmeans2.sh zisyo #3.3万から辞書作成
/media/chinourobot/HDCZ-UT/takayama/kmeans/code
2  ./jikoiti.sh #辞書の各点のdistance値
/media/chinourobot/HDCZ-UT/takayama/kmeans
3  ./kmeans_predict5.sh 2012-01-15　#テータベースとクリエの特徴量を辞書の特徴量クラス番号に置き換える
/media/chinourobot/HDCZ-UT/takayama/kmeans/result
4  python count.py 2012-01-15-result/f-1326652770479038.txt #clsの数確認
5  python find.py #エラーで処理できないものを検出するため、一般的にやる必要がない
/media/chinourobot/HDCZ-UT/takayama/kmeans
6  ./start-k-distance.sh #データベースとクエリ各点の間最短クラス（中身を変える必要がある）






