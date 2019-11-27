#!/bin/bash 

if [ $1 == "acc" ]
then
	sudo --stdin bash create_account.sh $2 $3 $4 < pass.lock

elif [ $1 == "pswd" ]
then
	sudo --stdion bash change_password.sh $2 $3 < pass.lock

elif [ $1 == "grp" ]
then
	sudo --stdin bash grp_owner.sh < pass.lock

fi

