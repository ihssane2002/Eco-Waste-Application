#!/bin/sh

# Wait for a few seconds to ensure the database is ready
sleep 3

# Initialize the database
flask db init
flask db migrate -m "Initial migration."
flask db upgrade

# Run the setup scripts
python articles.py
python map.py

# Start the Flask application
flask run --host=0.0.0.0