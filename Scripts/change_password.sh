#!/bin/bash

echo -e "$2\n$2" > .tmp
pdbedit -a $1 -t < .tmp
rm .tmp
