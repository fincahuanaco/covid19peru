day="2020-03-06"
last_day="2020-06-06"

newday=$(date -d "$day next day" +%Y-%m-%d); 

echo $newday
A=$day
B=$last_day
#echo $(( ( $last_day - $new_day )/(60*60*24) ))
#echo "scale=2; ( $last_day - $new_day )/(60*60*24)" | bc
days=`echo $(( ($(date -d $B +%s) - $(date -d $A +%s)) / 86400 ))`

for i in `seq 1 $days` 
do
    echo "$newday"
    # here you can use the section you want to use
    newday=$(date -d "$newday next day" +%Y-%m-%d); 
    echo $newday

    python3 ./drawperuseries.py $newday peruimages/frame$i.png
done
