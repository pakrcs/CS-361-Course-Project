# CS361 Course Project

This is my project for CS361. I created a Golf Tracker App with a variety of functionalities that demonstrate microservice structure.

## Clear instructions for how to programmatically REQUEST and RECEIVE data from the microservice you implemented. Include an example call.

Makes use of the request and Flask library in Python. Communication is done using Flask and HTTP requests. My microservice file, quotes.py, function is to randomly select quotes from a text file.

As an example, my microservice is being run on localhost:5002.

A GET request is made by the main program to the microservice.

The microservice responds to the GET request and sends a JSON response with the quote data.

The data received is then parsed and can be displayed however you want. This example just shows printing.

```python
import requests

# Make a GET request to the microservice endpoint
response = requests.get('http://localhost:5002/get_quote')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the quote data from the JSON response
    quote_data = response.json()
    quote = quote_data['quote']
    print("Quote:", quote)
else:
    print("Error:", response.text)
```

## UML sequence diagram showing how requesting and receiving data works. Make it detailed enough that your teammate (and your grader) will understand.

![UML Diagram](https://github.com/pakrcs/CS-361-Course-Project/assets/130027497/2672d15e-b737-4e45-a692-01f674358bae)
