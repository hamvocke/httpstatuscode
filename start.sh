#!/bin/bash

set -e

echo "Restarting/Reloading gunicorn server"

if [[ -f gunicorn.pid ]]; then
  echo "Found PID file, reloading gunicorn server"
  OLD_PID=$(cat gunicorn.pid)

  if [ -n $OLD_PID ]; then
    echo "Found PID: $OLD_PID"
    kill -HUP $OLD_PID
    echo "Reloaded gunicorn"
  fi
else
  echo "No previous PID file found"
  echo "Starting new gunicorn server"
  venv/bin/gunicorn app:app -c gunicorn.conf.py &
  PID=$!
  echo $PID > gunicorn.pid
fi

echo "Done"
exit
