#!/bin/bash 

useradd $1
echo "$2\n$2" > .tmp
pdbedit -a $1 -t < .tmp
rm .tmp
edquota -p gaetan $1 
usermod -aG $3 $1