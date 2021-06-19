hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-file /root/bidata_miniProject/autoinc_mapper2.py    -mapper /root/bidata_miniProject/autoinc_mapper2.py \
-file /root/bidata_miniProject/autoinc_reducer2.py   -reducer /root/bidata_miniProject/autoinc_reducer2.py \
-input /hadoopminiprk/data.csv \
-output /output