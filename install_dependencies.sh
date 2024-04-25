#!/bin/bash

echo "Installing dependencies"
sudo apt install nodejs
sudo apt install npm
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

sudo apt install python3
sudo apt install python3-pip
pip install pipenv
pip install flask-cors
pipenv install