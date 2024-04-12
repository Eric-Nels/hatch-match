#!/bin/bash

if lsof -i :3000; then
    echo "Terminating frontend..."
    kill $(lsof -t -i:3000)
fi

echo "Launching frontend..."
cd hatch-match-frontend
npm install
npm install \
  @testing-library/jest-dom@^5.17.0 \
  @testing-library/react@^13.4.0 \
  @testing-library/user-event@^13.5.0 \
  axios@^1.6.8 \
  react@^18.2.0 \
  react-dom@^18.2.0 \
  react-scripts@5.0.1 \
  web-vitals@^2.1.4
npm start &

sleep 5

echo "Launching backend..."
cd ../hatch-match-backend
sudo apt install python3
pip install flask-cors
pipenv install
sleep 5
pipenv run python seed.py
pipenv run python main.py

