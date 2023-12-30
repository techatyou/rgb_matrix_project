#!/bin/bash

# Define the path to your virtual environment and your Flask app
VENV_PATH="rgb_matrix_project/env"
APP_PATH="rgb_matrix_project/app.py"

# Check if the virtual environment directory exists
if [ ! -d "$VENV_PATH" ]; then
    echo "Virtual environment directory not found: $VENV_PATH"
    exit 1
fi

# Activate the virtual environment
echo "Activating the virtual environment..."
source "$VENV_PATH/bin/activate"

# Check if Flask is installed
if ! which flask > /dev/null; then
    echo "Flask not found in the virtual environment. Please install it using 'pip install Flask'."
    deactivate
    exit 1
fi

# Start the Flask web server
echo "Starting the Flask web server..."
FLASK_APP=$APP_PATH FLASK_ENV=development flask run

# Deactivate the virtual environment on script exit
deactivate
