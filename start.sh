#!/bin/sh
echo Start Server!

sudo gunicorn app:app -b 0.0.0.0:80 -w 2 --timeout=10 -k gevent

sudo ps -aux | grep gunicorn