#!/bin/bash
set -x
ls=`ls /home`

for dr in $ls
do
	if [ $dr != "gaetan" ]; then
		chown -R  :$dr "/home/$dr"
	fi
done
set +x
