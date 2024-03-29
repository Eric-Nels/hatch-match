#!/bin/bash

if lsof -i :3000; then
    echo "Terminating frontend..."
    kill $(lsof -t -i:3000)
fi

echo "Launching frontend..."
cd hatch-match-frontend
npm install
npm install axios
npm start &

sleep 5

echo "Launching backend..."
cd ../hatch-match-backend
pip install flask-cors
pipenv install
sleep 5
pipenv run python seed.py
pipenv run python main.py

