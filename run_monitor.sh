#!/bin/bash
# Start Flask app in the background
python3 app.py &
APP_PID=$!
echo "Flask app started with PID $APP_PID"

# Infinite loop to run health_check every 10 seconds
while true; do
    python3 health_check.py
    sleep 10
done
