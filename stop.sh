#!/bin/bash

set -e

echo "Gracefully stopping gunicorn server"

if [[ -f gunicorn.pid ]]; then
  echo "Found PID file, stopping gunicorn server"
  OLD_PID=$(cat gunicorn.pid)

  if [ -n $OLD_PID ]; then
    echo "Found PID: $OLD_PID"
    kill -TERM $OLD_PID
    rm -f gunicorn.pid
    echo "Stopped gunicorn"
  fi
else
  echo "No PID file found, nothing to stop"
fi

exit
