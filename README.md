# GeneratePasswordApi
## Objective 
Develop a Rest API using FastAPI that allows users to request new passwords based on specified criteria.

Requirements
1. API endpoint: create an endpoint `/generate-password` which accepts POST requests.
2. Request Payload: the endpoint should accept a JSON payload that contains a `length` field
that indicates the length of the password to be returned. If you would like to add any
additional fields to improve the password generation then please do.
3. Password generation logic: using the fields given in the request payload, generate a
password.
4. Response: return a JSON response with the generated password.
5. Error handling: implement error handling for invalid inputs.
6. Testing: write a unit test or two for the password generation logic you created in a previous
step.


## Technology Used
* Python
* FastApi
* uvicorn

## Getting started
  Ensure that you have Python installed on your machine before setting up the GeneratePasswordApi project. If Python is not installed, you can download and install it from the [official Python website](https://www.python.org/downloads/).
   
1. **Clone the Repository to your local machine:**
    
2. **Create a Virtual Environment:**
    * python -m venv venv
      
      #### For Unix/Mac :
    * source venv/bin/activate
      #### For Windows  :
    * venv\Scripts\activate
      
3. **Install Dependencies:**
   * pip install -r requirements.txt

4. **Run the FastAPI Server:**
   * uvicorn main:app --reload
5. **Enter local url or below url in browser :**
   * http://127.0.0.1:8000/docs


![FastAPI-Swagger-UI](https://github.com/rajprashant84/GeneratePasswordApi/assets/63925713/6fc726b3-3d26-48b2-acda-ead111054d7c)


