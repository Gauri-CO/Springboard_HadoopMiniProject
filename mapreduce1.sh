hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-file /root/bidata_miniProject/autoinc_mapper1.py    -mapper /root/bidata_miniProject/autoinc_mapper1.py \
-file /root/bidata_miniProject/autoinc_reducer1.py   -reducer /root/bidata_miniProject/autoinc_reducer1.py \
-input /hadoopminiprk/data.csv \
-output /output