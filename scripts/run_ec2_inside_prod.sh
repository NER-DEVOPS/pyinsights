#!/bin/bash

cd /opt/pyinsights/

for x in ./queries/all_*.yml;
do echo $x;
   name=$(echo $x | cut "-d/" -f3)
   echo $name
   #if [ ! -f ./data/prod_${name} ]; then
   pyinsights -c  ${x} --profile prod -r us-east-1 > ./data/prod_${name}
   #else
   #    echo skip $name
   #fi
done
