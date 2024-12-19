# Introduction to My Flask Application

Welcome to my Flask application! This application is designed to manage a hierarchical structure of continents, countries, and cities. It provides a RESTful API that allows users to perform CRUD (Create, Read, Update, Delete) operations on these entities.

## Key Features

- **Continents Management**: Create, read, update, and delete continents.
- **Countries Management**: Create, read, update, and delete countries within a specific continent.
- **Cities Management**: Create, read, update, and delete cities within a specific country.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **Flask-RESTX**: An extension for Flask that adds support for quickly building REST APIs.
- **Docker**: A platform for developing, shipping, and running applications in containers.
- **Docker Compose**: A tool for defining and running multi-container Docker applications.

## Project Structure

- **app.py**: The main application file that defines the API endpoints and their corresponding logic.
- **test_app.py**: A test module for testing the functionality of `app.py`.
- **data_handler.py**: A helper module for reading and writing JSON data.
- **test_data_handler.py**: A test module for testing the functionality of `data_handler.py`.
- **Data.json**: A JSON file that stores the hierarchical data of continents, countries, and cities.
- **Dockerfile**: A file that defines the Docker image for the application.
- **docker-compose.yml**: A file that defines the services and their configurations for Docker Compose.

## Getting Started

To get started with the application, follow these steps:

1. **Clone the Repository**:
   ```sh
   git clone <repository-url>
   cd <repository-directory>

2. **Build and Run the Docker Compose Services**:
   ```sh
    docker-compose up --build

3. **Access the Application**: Open your web browser and navigate to http://localhost:5000. 

## Testing Instructions

1. To run tests for the application run pytest
   ```sh
    pytest test_data_handler.py
    pytest test_app.py 

2. Verify Test Results: Check the output of the pytest command to ensure all tests pass.

# API Endpoint Instructions

This section provides instructions on how to use the API endpoints for managing continents, countries, and cities in your Flask application.

## Base URL

The base URL for all API endpoints is:
http://localhost:5000/data

## Endpoints

### Continents

- **List all continents**
  - **Endpoint**: `/continents`
  - **Method**: `GET`
  - **Description**: Retrieves a list of all continents.
  - **Example**:
    ```sh
    curl -X GET http://localhost:5000/data/continents
    ```

- **Create a new continent**
  - **Endpoint**: `/continents`
  - **Method**: `POST`
  - **Description**: Creates a new continent.
  - **Example**:
    ```sh
    curl -X POST http://localhost:5000/data/continents -H "Content-Type: application/json" -d '{"name": "Europe", "countries": []}'
    ```

- **Get a specific continent**
  - **Endpoint**: `/continents/{continent_name}`
  - **Method**: `GET`
  - **Description**: Retrieves details of a specific continent.
  - **Example**:
    ```sh
    curl -X GET http://localhost:5000/data/continents/Europe
    ```

- **Delete a continent**
  - **Endpoint**: `/continents/{continent_name}`
  - **Method**: `DELETE`
  - **Description**: Deletes a specific continent.
  - **Example**:
    ```sh
    curl -X DELETE http://localhost:5000/data/continents/Europe
    ```

### Countries

- **List all countries in a continent**
  - **Endpoint**: `/continents/{continent_name}/countries`
  - **Method**: `GET`
  - **Description**: Retrieves a list of all countries in a specific continent.
  - **Example**:
    ```sh
    curl -X GET http://localhost:5000/data/continents/Africa/countries
    ```

- **Create a new country in a continent**
  - **Endpoint**: `/continents/{continent_name}/countries`
  - **Method**: `POST`
  - **Description**: Creates a new country in a specific continent.
  - **Example**:
    ```sh
    curl -X POST http://localhost:5000/data/continents/Africa/countries -H "Content-Type: application/json" -d '{"name": "Kenya", "cities": ["Nairobi", "Mombasa"]}'
    ```

- **Get the continent of a given country**
  - **Endpoint**: `/data/countries/{country_name}/continent`
  - **Method**: `GET`
  - **Description**: Retrieves the continent of a given country.
  - **Example**:
    ```sh
    curl -X GET http://localhost:5000/data/countries/Nigeria/continent
    ```

- **Get the continent of a given country**
  - **Endpoint**: `/countries/{country_name}/continent`
  - **Method**: `GET`
  - **Description**: Retrieves the continent of a given country.
  - **Example**:
    ```sh
    curl -X GET http://localhost:5000/data/countries/Nigeria/continent
    ```

### Cities

- **List all cities in a country**
  - **Endpoint**: `/continents/{continent_name}/countries/{country_name}/cities`
  - **Method**: `GET`
  - **Description**: Retrieves a list of all cities in a country.
  - **Example**:
    ```sh
    curl -X GET http://localhost:5000/data/continents/Africa/countries/Nigeria/cities
    ```

- **Create a new city in a country**
  - **Endpoint**: `/continents/{continent_name}/countries/{country_name}/cities`
  - **Method**: `POST`
  - **Description**: Creates a new city in a country.
  - **Example**:
    ```sh
    curl -X POST http://localhost:5000/data/continents/Africa/countries/Nigeria/cities -H "Content-Type: application/json" -d '{"name": "Ibadan"}'
    ```

- **Get a specific city in a country**
  - **Endpoint**: `/continents/{continent_name}/countries/{country_name}/cities/{city_name}`
  - **Method**: `GET`
  - **Description**: Retrieves a specific city in a country.
  - **Example**:
    ```sh
    curl -X GET http://localhost:5000/data/continents/Africa/countries/Nigeria/cities/Ibadan
    ```

- **Update a city in a country**
  - **Endpoint**: `/continents/{continent_name}/countries/{country_name}/cities/{city_name}`
  - **Method**: `PUT`
  - **Description**: Updates a city in a country.
  - **Example**:
    ```sh
    curl -X PUT http://localhost:5000/data/continents/Africa/countries/Nigeria/cities/Ibadan -H "Content-Type: application/json" -d '{"name": "Ibadan"}'
    ```

- **Delete a city in a country**
  - **Endpoint**: `/continents/{continent_name}/countries/{country_name}/cities/{city_name}`
  - **Method**: `DELETE`
  - **Description**: Deletes a city in a country.
  - **Example**:
    ```sh
    curl -X DELETE http://localhost:5000/data/continents/Africa/countries/Nigeria/cities/Ibadan
    ```

By following these instructions and using the provided `curl` commands, you can easily manage the hierarchical structure of continents, countries, and cities in your Flask application.
