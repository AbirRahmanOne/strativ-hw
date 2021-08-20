# strativ
* Python Developer Assignment [Strativ]

## Project Run Instructions:
### Create a virtual environment to isolate our package dependencies locally
* `python3 -m venv env`
* `source env/bin/activate`  # On Windows use `env\Scripts\activate`
### Install all dependencies 
* `pip install -r requirements.txt`
* `pip freeze > requirements.txt`
  
### Adding Countries Instructions:
* Open Terminal
* Go to project directory
* Type `python manage.py migrate`
* Type `python manage.py seed`

### Project Run Instructions:
* Open Terminal
* Go to project directory
* Create Super User 
   * Type  `python manage.py createsuperuser`
  
* Type `python manage.py runserver`


## API Overview (Example):
### Create token
* `http://localhost:8000/token`
    * method: 'POST'
  
### Country CRUD Operation
* Get all countries list:
    * `http://localhost:8000/api/countries`
    * Method: `GET`
* Get specific country details:
     * `http://localhost:8000/api/country/1`
     * Method: `GET`
* Create specific country details:
     * `http://localhost:8000/api/countries`
     * Method: `POST`
* Update specific country details:
     * `http://localhost:8000/api/country/id`
     * Here id -> 1,2,
     * Method: `PATCH`
* Delete specific country details:
     * `http://localhost:8000/api/country/id`
     * Method: `DELETE`
### List of neighbouring countries of an specific country
* Type: `http://localhost:8000/api/countries?neighbouring_country==AFG`
    * Method: GET 

### List of countries who speaks the same language based on a specific language
* Type: `http://localhost:8000/api/countries?same_language_country=Bengali`
    * Method: GET 
### Searching a country by its name (should be able to search partial name)
* Type: `http://localhost:8000/api/countries?name=bang`
    * Method: GET

* Full demo `http://localhost:8000/api/countries?name=&neighbouring_country=AFG&same_language_country=`
  



