#!/bin/bash

if lsof -i :3000; then
    echo "Terminating frontend..."
    kill $(lsof -t -i:3000)
fi

echo "Launching frontend..."
cd hatch-match-frontend
npm start &

echo "Launching backend..."
cd ../hatch-match-backend
pipenv run python seed.py
pipenv run python main.py
