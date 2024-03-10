#!/bin/bash

echo "Cloning the repository..."
git clone https://github.com/v4k0nd/erma-py-flask.git
cd erma-py-flask

echo "Creating a virtual environment..."
python3 -m venv .venv

echo "Activating the virtual environment..."
source .venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Copying .env.example to .env..."
cp .env.example .env


echo "Setup complete. Please customize your .env file as needed."

echo "Then you can run the Flask application using 'flask run'."