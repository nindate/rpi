#!/bin/bash

maxcount=10
capturedir="/cctv/capture"
allowedusagepct=1    #disk space used in percentage
capturetime=10000        #time in milli seconds

i=0
while true  #[[ i -lt $maxcount ]]
do
echo $i
let "i=i+1"
usagepct=$(df -h ${capturedir} | grep -v Filesystem | awk '{print $5}' | sed "s/\%//g")
echo "Capture directory is $usagepct % utilised"
if [[ $usagepct -le $allowedusagepct ]]
 then
    echo "Utilisation within limit"
 else
    echo "Utlisation over allowed limit"
fi
raspivid -o ${capturedir}/capture-${i}.h264 -t $capturetime
sleep 1
done
