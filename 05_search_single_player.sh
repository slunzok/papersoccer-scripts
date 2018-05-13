FILE=labs/spis

# For week #1, I ran test for player: skromny18 (150 matches, 106 wins, 44 losses
# ./05_search_player root
# ./07_ls_replays.py root
# python ./08_generate_stats.py

if [ ! -d "gracze/$1" ]; then
  # Control will enter here if $DIRECTORY exists.
  mkdir "gracze/$1"
  mkdir "gracze/$1/00_$1"
  touch "gracze/$1/"$1"_broken.txt"
  touch "gracze/$1/"$1"_stats.csv"
  echo "id,name,rank,sums,games,wins,losses" >> gracze/$1/"$1"_stats.csv
fi

while read line;
do
    DATE=${line:0:10}
    FIRST_FILE=${line:11:8}
    LAST_FILE=${line:20:8}
    echo $DATE $FIRST_FILE $LAST_FILE
    python 06_analyze_user_replay.py $DATE $FIRST_FILE $LAST_FILE $1
done < $FILE
