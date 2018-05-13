FILE=labs/spis
while read line;
do
    DATE=${line:0:10}
    FIRST_FILE=${line:11:8}
    LAST_FILE=${line:20:8}
    echo $DATE $FIRST_FILE $LAST_FILE
    python 04_binary_search.py $DATE $FIRST_FILE $LAST_FILE
done < $FILE
