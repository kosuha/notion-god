#!/bin/sh

process_id=`sudo ps -ef | grep -v "grep" | grep "app" | awk '{print $2}'`
if [ "$process_id" != "" ]
then
	echo "프로세스 PID : $process_id"
	sudo kill $process_id
fi

echo Server closed!