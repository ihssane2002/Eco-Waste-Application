<header>

<!--
  <<< Author notes: Course header >>>
  Include a 1280×640 image, course title in sentence case, and a concise description in emphasis.
  In your repository settings: enable template repository, add your 1280×640 social image, auto delete head branches.
  Add your open source license, GitHub uses MIT license.
-->

# Application de Gestion des dechets

_TDLog Project._

</header>


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv myenv
    myenv\Scripts\activate 
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```


4. Initialize the database:
    ```sh
    python -m flask db init  
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

5. Run these Scripts

- [articles.py](http://_vscodecontentref_/10): Script to add articles to the database.
- [map.py](http://_vscodecontentref_/11): Script to initialize collection points and add them manually to the database.

## Running the Application

1. Start the Flask development server:
    ```sh
    flask run
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.


## Running tests
python -m unittest tests.py#   A p p l i c a t i o n _ T D L O G _ 2 A 
 
 #   A p p l i c a t i o n _ T D L O G _ 2 A 
 
 