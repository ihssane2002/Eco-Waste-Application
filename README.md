# Eco Waste Application

## A web application for managing and tracking eco-friendly waste collection.

# Option 1
## Installation

1. Clone the repository:
    ---
- git clone https://github.com/Saharbenrejab0/Application_TDLog.git
- cd Application_TDLog
    

2. Create a virtual environment and activate it:
    
- python -m venv myenv
- myenv\Scripts\activate 
    

3. Install the dependencies:
    
- pip install -r requirements.txt
    


4. Initialize the database:
    
- python -m flask db init  
- flask db migrate -m "Initial migration."
- flask db upgrade
    

5. Run these Scripts

- [articles.py](http://vscodecontentref/10): Script to add articles to the database.
- [map.py](http://vscodecontentref/11): Script to initialize collection points and add them manually to the database.

## Running the Application

1. Start the Flask development server:
    
- flask run
    

2. Open your web browser and go to http://127.0.0.1:5000/.


# Option 2: Using Docker

1. Clone the repository:
- git clone https://github.com/Saharbenrejab0/Application_TDLog.git
- cd Application_TDLog

2. Build the Docker image:
- docker build -t flask-app .

3. Create a volume for the database:
- docker volume create flask-db-data

4. Run the container:
- docker run -d -p 5000:5000 -v flask-db-data:/app/instance --name my-flask-app fla
## Running the Application

- After running the container, open your web browser and go to http://127.0.0.1:5000/


# Option 3 : cloning our docker image

Prerequisites

1. Docker installed on your machine (Get Docker)

2. Running the Application

**Pull the Docker image**:

- ydocker pull saharbenrejab0/ecowaste:latest

**Create a volume for database persistence**:

- docker volume create flask-db-data

**Run the container**:

- docker run -d -p 5000:5000 -v flask-db-data:/app/instance --name eco-waste saharbenrejab0/ecowaste

**Access the application**:

- Open your web browser
Go to http://localhost:5000

# Running tests
- python -m unittest tests.py
