#!/bin/bash

# Create and activate a new virtual environment
python -m venv .env
source .env/Scripts/activate

# Install the required packages
pip install -r requirements.txt

# Run the server
python manage.py runserver
