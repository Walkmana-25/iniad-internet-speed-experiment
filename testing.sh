#! /bin/bash
for i in `seq 3`
do
    date >> output.txt
    speedtest -s 14623 >> output.txt
done