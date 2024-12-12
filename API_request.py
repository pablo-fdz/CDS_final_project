import requests
import json
import pandas as pd

# Define the API endpoint ( "/predict")
url = "http://127.0.0.1:8000/predict"

# Load the input data from JSON 
def load_input_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return None
    except json.JSONDecodeError:
        print("Error: The file contains invalid JSON.")
        return None

# Function to send a POST request
def get_prediction(input_data):
    try:
        # Send the POST request with JSON data
        response = requests.post(url, json=input_data)
        
        # Raise an exception for status codes that indicate an error
        response.raise_for_status()
        
        # Parse and print the response
        prediction = response.json()

        #print response in table format
        print(f"Prediction: {pd.DataFrame(prediction)}")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the API.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
    except json.JSONDecodeError:
        print("Error: Unable to parse response as JSON.")

#--------------------------------------------------------
#---------------------request----------------------------

# Load data from the JSON file and send prediction request if data is valid
input_file = "data/prediction_request.json"
input_data = load_input_data(input_file)

if input_data:
    get_prediction(input_data)
