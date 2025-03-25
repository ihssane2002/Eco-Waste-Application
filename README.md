# Eco Waste Application
Description :
Le projet Eco Waste Application vise à concevoir une application de gestion des déchets permettant aux utilisateurs de suivre leurs pratiques de recyclage et d’adopter des comportements écoresponsables.
Avec Eco Waste Application, l’idée est simple : nous vous accompagneons  pour rendre le tri et le recyclage plus faciles, plus amusants, et surtout, plus impactants ! Ensemble, faisons un pas de plus vers un mode de vie respectueux de la planète.
Fonctionnalités principales :

Enregistrement et suivi des déchets.
Cartographie des points de recyclage.
Notifications de rappel pour encourager le tri et le recyclage.
Gamification pour motiver les utilisateurs.
L’objectif est de fournir une expérience utilisateur fluide, engageante et personnalisée, adaptée aussi bien aux novices qu’aux utilisateurs confirmés. Grâce à cette application, chacun peut contribuer à la préservation de l’environnement tout en s’amusant et en apprenant au quotidien.

## A web application for managing and tracking eco-friendly waste collection.
# for waste management
# Option 1
## Installation

1. Clone the repository:
    ---
- git clone https://github.com/ihssane2002/Eco-Waste-Application.git
- cd Eco-Waste-Application
    

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
- git clone https://github.com/ihssane2002/Eco-Waste-Application.git
- cd Eco-Waste-Application

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

**Docker installed on your machine (Get Docker)**

**Running the Application**

1. Pull the Docker image:

- docker pull ihssane2002/ecowaste:latest

2. Create a volume for database persistence:

- docker volume create flask-db-data

3. Run the container:

- docker run -d -p 5000:5000 -v flask-db-data:/app/instance --name eco-waste ihssane2002/ecowaste

4. Access the application:

- Open your web browser
Go to http://localhost:5000

# Running tests
- python -m unittest tests.py
# Integration de frontend 
-  Ce projet frontend est conçu pour être intégré avec l'application backend développée avec Flask, permettant une gestion centralisée et offre une interface utilisateur sophistiqué. Cette combinaison assurera une application full-stack fonctionnelle,Ce code est intégré dans le branch integration-frontend 
