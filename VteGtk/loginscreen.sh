#!/bin/bash
function neo
{   
    m=$*;n=${#m};i=0
    while [ $i -lt $n ];do
        sleep 0.05
        echo -n "${m:$i:1}" 
        ((i+=1))
    done;echo 
}
clear
neo "Wake up , Neo"
sleep 1 && clear
neo "The matrix has you"
sleep 1 && clear
neo "Follow the white rabbit"
sleep 1 && clear
neo "Knock knock Neo"
sleep 1 && clear