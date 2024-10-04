#! /bin/bash
for i in `seq 3`
do
    date >> /home/ubuntu/output.txt
    speedtest -s 14623 --accept-license | grep -e 'Idle Latency' -e 'Download' -e 'Upload' >> /home/ubuntu/output.txt
done