#!/bin/bash  
# shell for running fastapi server

echo "Installing pip3"
sudo apt-get install python3-pip

echo "Configuring Virtual Environemt"

echo "Environment setup"
echo "Creating Vertual environmet named dev"
python3 -m venv dev/

echo "Environment active"
source dev/bin/activate

echo "installing dependencies"
sudo pip3 install -r requirements.txt

echo "Running server"
uvicorn app:app --reload

