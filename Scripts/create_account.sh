#!/bin/bash

useradd $1
echo -e "$2\n$2" > .tmp
cat .tmp
pdbedit -a $1 -t < .tmp
rm .tmp
edquota -p gaetan $1
usermod -aG $3 $1
