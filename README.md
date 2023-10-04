# backportfolio

Simple RESTful API with Flask
This repository contains a sample RESTful API built with Flask, a popular web framework for Python. The API allows you to perform basic CRUD (Create, Read, Update, Delete) operations on user data stored in-memory.

Features
Create User: You can create a new user by sending a POST request to the /users endpoint with user details in the request body.

Get All Users: Retrieve a list of all users by making a GET request to the /users endpoint.

Get User by ID: Fetch a specific user's details by providing their unique ID in a GET request to /user/{user_id}.

Update User: Update user information by sending a PUT request to /user/{user_id} with the modified user data.

Delete User: Delete a user by making a DELETE request to /user/{user_id}.

CORS Configuration: Cross-Origin Resource Sharing (CORS) is configured to allow requests from a specific origin, enabling cross-domain API access.

Usage
Clone this repository to your local machine.

Install the required dependencies using pip install -r requirements.txt.

Run the Flask application with python app.py.

You can now interact with the API using your preferred API client (e.g., Postman, curl) or integrate it into your web application.

Ensure that CORS is configured correctly for your application's frontend.

API Endpoints
POST /users: Create a new user.
GET /users: Retrieve a list of all users.
GET /user/{user_id}: Retrieve a specific user by ID.
PUT /user/{user_id}: Update a user's information.
DELETE /user/{user_id}: Delete a user.
CORS Configuration
CORS (Cross-Origin Resource Sharing) is configured to allow requests from a specific origin, https://ubiquitous-crostata-c9a03d.netlify.app. This enables your frontend to communicate with the API seamlessly.

Contributing
If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request. We welcome contributions!

License
This project is licensed under the MIT License. Feel free to use, modify, or distribute it as needed.

Feel free to customize this README to include any additional information specific to your project. Enjoy building with Flask!
