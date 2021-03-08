#!/bin/bash

cd /opt/pyinsights/

for x in ./queries/all_*.yml;
do echo $x;
   name=$(echo $x | cut "-d/" -f3)
   echo $name
   echo ./data/dev_${name}
   pyinsights -c  ${x} --profile default -r us-east-1 > ./data/dev_${name}
done
