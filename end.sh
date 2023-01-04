#!/bin/sh

process_id=`ps -ef | grep -v "grep" | grep "app" | awk '{print $2}'`
if [ "$process_id" != "" ]
then
	echo "프로세스 PID : $process_id"
	kill $process_id
fi

echo Server closed!