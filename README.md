# data_rep_project
Data Representation Project

Required Packages:

1. flask
2. flask_restful
3. flask_sqlalchemy

The Flask application incorporates the Flask-RESTful API for handling CRUD operations on items and includes web pages for viewing, adding, and deleting items. Below is a summary of the key components:

Flask App Configuration:

The app is configured with an SQLite database using Flask-SQLAlchemy.
An instance of the app, Flask-RESTful API, and SQLAlchemy are created.

Database Model:

The Item class is defined as a simple model with an id (primary key) and a name field.

RESTful API Resource:

The ItemResource class is created to handle RESTful API operations (GET, PUT, DELETE) on individual items.
API Endpoint Registration:


