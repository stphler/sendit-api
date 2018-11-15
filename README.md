SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.
Getting Started

Clone or download the project from git either via terminal using the commands

    git clone :https://github.com/Mark9Mbugua/SendITAPI.git
    Download zip file from the right hand corner

Use the following endpoints to perform the specified tasks
Endpoint 	                      Functionality
GET /parcels                      Fetch all parcel delivery orders
GET /parcels/<parcelId>           Fetch a specific parcel delivery order
GET /users/<userId>/parcels       Fetch all parcel delivery orders by a specific user
PUT /parcels/<parcelId>/cancel    Cancel the specific parcel delivery order
POST /parcels                     Create a parcel delivery order

     A User can create a parcel delivery order.
    Admin page for managing parcel deliveries by Users.

Users can do the following

    Users can create an account and log in.
    Users can request a parcel delivery.
    Users can cancel a delivery request.
    Users can view all deliveries that they have requested.
    Users can view a specific delivery.

Requirements

Ensure you have a browser such as firefox or chrome installed.

Make sure you download postman to be able to test the specific endpoints on this project.
Running

    git clone https://github.com/stphler/sendit-api
    cd into folder
    create a virtual enviroment using virtualenv env
    activate env
    export FLASP_APP=run.py
    export FLASK_ENV=development
    flask run

[![Coverage Status](https://coveralls.io/repos/github/stphler/sendit-api/badge.svg)](https://coveralls.io/github/stphler/sendit-api)