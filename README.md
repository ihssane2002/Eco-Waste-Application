# Eco Waste Application
## Installation

1. Clone the repository:
    sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    

2. Create a virtual environment and activate it:
    sh
    python -m venv myenv
    myenv\Scripts\activate 
    

3. Install the dependencies:
    sh
    pip install -r requirements.txt
    


4. Initialize the database:
    sh
    python -m flask db init  
    flask db migrate -m "Initial migration."
    flask db upgrade
    

5. Run these Scripts

- [articles.py](http://vscodecontentref/10): Script to add articles to the database.
- [map.py](http://vscodecontentref/11): Script to initialize collection points and add them manually to the database.

## Running the Application

1. Start the Flask development server:
    sh
    flask run
    

2. Open your web browser and go to http://127.0.0.1:5000/.


## Running tests
python -m unittest tests.py
