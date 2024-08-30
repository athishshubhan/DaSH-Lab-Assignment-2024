#!/bin/bash

# Navigate to the project directory
cd /Users/athis/DaSH-Lab-Assignment-2024

# Activate the virtual environment
source venv/bin/activate

# Start the server
python3 server.py &

# Wait for server to start
sleep 2

# Launch multiple clients
python3 client.py input.txt 1 &
python3 client.py input.txt 2 &
python3 client.py input.txt 3 &
python3 client.py input.txt 4 &

# Wait for all clients to finish
wait

# Deactivate the virtual environment
deactivate
