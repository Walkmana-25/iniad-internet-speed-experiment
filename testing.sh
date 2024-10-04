#! /bin/bash
for i in `seq 3`
do
    date >> /home/ubuntu/output.txt
    speedtest -s 14623 >> /home/ubuntu/output.txt
done