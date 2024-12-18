from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from urllib.parse import quote as url_quote
from data_handler import read_json, write_json
import os

app = Flask(__name__)
api = Api(app, version='1.0', title='My API',
          description='A simple API',
          )

ns = api.namespace('data', description='Data operations')

# Configurable parameter for the JSON file
json_filename = 'Data.json'

# Ensure the JSON file exists
if not os.path.exists(json_filename):
    print(f"{json_filename} does not exist. Creating a new file.")
    data = {"continents": []}
    write_json(json_filename, data)

continent_model = api.model('Continent', {
    'name': fields.String(required=True, description='The continent name'),
    'countries': fields.List(fields.Nested(api.model('Country', {
        'name': fields.String(required=True, description='The country name'),
        'cities': fields.List(fields.String, description='List of cities')
    })), description='List of countries')
})

country_model = api.model('Country', {
    'name': fields.String(required=True, description='The country name'),
    'cities': fields.List(fields.String, description='List of cities')
})

city_model = api.model('City', {
    'name': fields.String(required=True, description='The city name')
})

@ns.route('/continents')
class ContinentList(Resource):
    @ns.doc('list_continents')
    def get(self):
        '''List all continents'''
        data = read_json(json_filename)
        if data is None:
            return {"error": "Failed to read data"}, 500
        return data['continents']

    @ns.doc('create_continent')
    @ns.expect(continent_model)
    def post(self):
        '''Create a new continent'''
        data = read_json(json_filename)
        if data is None:
            return {"error": "Failed to read data"}, 500
        new_continent = request.json
        data['continents'].append(new_continent)
        write_json(json_filename, data)
        return new_continent, 201

@ns.route('/continents/<string:name>')
@ns.response(404, 'Continent not found')
@ns.param('name', 'The continent name')
class Continent(Resource):
    @ns.doc('get_continent')
    def get(self, name):
        '''Fetch a given continent'''
        data = read_json(json_filename)
        if data is None:
            return {"error": "Failed to read data"}, 500
        continent = next((c for c in data['continents'] if c['name'] == name), None)
        if continent is None:
            return {"error": "Continent not found"}, 404
        return continent

    @ns.doc('delete_continent')
    def delete(self, name):
        '''Delete a continent'''
        data = read_json(json_filename)
        if data is None:
            return {"error": "Failed to read data"}, 500
        continent = next((c for c in data['continents'] if c['name'] == name), None)
        if continent is None:
            return {"error": "Continent not found"}, 404
        data['continents'].remove(continent)
        write_json(json_filename, data)
        return '', 204

    @ns.doc('update_continent')
    @ns.expect(continent_model)
    def put(self, name):
        '''Update a continent'''
        data = read_json(json_filename)
        if data is None:
            return {"error": "Failed to read data"}, 500
        continent = next((c for c in data['continents'] if c['name'] == name), None)
        if continent is None:
            return {"error": "Continent not found"}, 404
        updated_continent = request.json
        continent.update(updated_continent)
        write_json(json_filename, data)
        return continent

@ns.route('/continents/<string:continent_name>/countries')
class CountryList(Resource):
    @ns.doc('list_countries')
    def get(self, continent_name):
        '''List all countries in a continent'''
        data = read_json(json_filename)
        if data is None:
            return {"error": "Failed to read data"}, 500
        continent = next((c for c in data['continents'] if c['name'] == continent_name), None)
        if continent is None:
            return {"error": "Continent not found"}, 404
        return continent['countries']

    @ns.doc('create_country')
    @ns.expect(country_model)
    def post(self, continent_name):
        '''Create a new country in a continent'''
        data = read_json(json_filename)
        if data is None:
            return {"error": "Failed to read data"}, 500
        continent = next((c for c in data['continents'] if c['name'] == continent_name), None)
        if continent is None:
            return {"error": "Continent not found"}, 404
        new_country = request.json
        continent['countries'].append(new_country)
        write_json(json_filename, data)
        return new_country, 201

@ns.route('/continents/<string:continent_name>/countries/<string:country_name>')
@ns.response(404, 'Country not found')
@ns.param('continent_name', 'The continent name')
@ns.param('country_name', 'The country name')
class Country(Resource):
    @ns.doc('get_country')
    def get(self, continent_name, country_name):
        '''Fetch a given country in a continent'''
        data = read_json(json_filename)
        if data is None:
            return {"error": "Failed to read data"}, 500
        continent = next((c for c in data['continents'] if c['name'] == continent_name), None)
        if continent is None:
            return {"error": "Continent not found"}, 404
        country = next((c for c in continent['countries'] if c['name'] == country_name), None)
        if country is None:
            return {"error": "Country not found"}, 404
        return country

    @ns.doc('delete_country')
    def delete(self, continent_name, country_name):
        '''Delete a country in a continent'''
        data = read_json(json_filename)
        if data is None:
            return {"error": "Failed to read data"}, 500
        continent = next((c for c in data['continents'] if c['name'] == continent_name), None)
        if continent is None:
            return {"error": "Continent not found"}, 404
        country = next((c for c in continent['countries'] if c['name'] == country_name), None)
        if country is None:
            return {"error": "Country not found"}, 404
        continent['countries'].remove(country)
        write_json(json_filename, data)
        return '', 204

    @ns.doc('update_country')
    @ns.expect(country_model)
    def put(self, continent_name, country_name):
        '''Update a country in a continent'''
        data = read_json(json_filename)
        if data is None:
            return {"error": "Failed to read data"}, 500
        continent = next((c for c in data['continents'] if c['name'] == continent_name), None)
        if continent is None:
            return {"error": "Continent not found"}, 404
        country = next((c for c in continent['countries'] if c['name'] == country_name), None)
        if country is None:
            return {"error": "Country not found"}, 404
        updated_country = request.json
        country.update(updated_country)
        write_json(json_filename, data)
        return country

@ns.route('/continents/<string:continent_name>/countries/<string:country_name>/cities')
class CityList(Resource):
    @ns.doc('list_cities')
    def get(self, continent_name, country_name):
        '''List all cities in a country'''
        data = read_json(json_filename)
        if data is None:
            return {"error": "Failed to read data"}, 500
        continent = next((c for c in data['continents'] if c['name'] == continent_name), None)
        if continent is None:
            return {"error": "Continent not found"}, 404
        country = next((c for c in continent['countries'] if c['name'] == country_name), None)
        if country is None:
            return {"error": "Country not found"}, 404
        return country['cities']

    @ns.doc('create_city')
    @ns.expect(city_model)
    def post(self, continent_name, country_name):
        '''Create a new city in a country'''
        data = read_json(json_filename)
        if data is None:
            return {"error": "Failed to read data"}, 500
        continent = next((c for c in data['continents'] if c['name'] == continent_name), None)
        if continent is None:
            return {"error": "Continent not found"}, 404
        country = next((c for c in continent['countries'] if c['name'] == country_name), None)
        if country is None:
            return {"error": "Country not found"}, 404
        new_city = request.json
        country['cities'].append(new_city['name'])
        write_json(json_filename, data)
        return new_city, 201

@ns.route('/continents/<string:continent_name>/countries/<string:country_name>/cities/<string:city_name>')
@ns.response(404, 'City not found')
@ns.param('continent_name', 'The continent name')
@ns.param('country_name', 'The country name')
@ns.param('city_name', 'The city name')
class City(Resource):
    @ns.doc('get_city')
    def get(self, continent_name, country_name, city_name):
        '''Fetch a given city in a country'''
        data = read_json(json_filename)
        if data is None:
            return {"error": "Failed to read data"}, 500
        continent = next((c for c in data['continents'] if c['name'] == continent_name), None)
        if continent is None:
            return {"error": "Continent not found"}, 404
        country = next((c for c in continent['countries'] if c['name'] == country_name), None)
        if country is None:
            return {"error": "Country not found"}, 404
        city = next((c for c in country['cities'] if c == city_name), None)
        if city is None:
            return {"error": "City not found"}, 404
        return {"name": city}

    @ns.doc('delete_city')
    def delete(self, continent_name, country_name, city_name):
        '''Delete a city in a country'''
        data = read_json(json_filename)
        if data is None:
            return {"error": "Failed to read data"}, 500
        continent = next((c for c in data['continents'] if c['name'] == continent_name), None)
        if continent is None:
            return {"error": "Continent not found"}, 404
        country = next((c for c in continent['countries'] if c['name'] == country_name), None)
        if country is None:
            return {"error": "Country not found"}, 404
        city = next((c for c in country['cities'] if c == city_name), None)
        if city is None:
            return {"error": "City not found"}, 404
        country['cities'].remove(city)
        write_json(json_filename, data)
        return '', 204

    @ns.doc('update_city')
    @ns.expect(city_model)
    def put(self, continent_name, country_name, city_name):
        '''Update a city in a country'''
        data = read_json(json_filename)
        if data is None:
            return {"error": "Failed to read data"}, 500
        continent = next((c for c in data['continents'] if c['name'] == continent_name), None)
        if continent is None:
            return {"error": "Continent not found"}, 404
        country = next((c for c in continent['countries'] if c['name'] == country_name), None)
        if country is None:
            return {"error": "Country not found"}, 404
        city_index = next((i for i, c in enumerate(country['cities']) if c == city_name), None)
        if city_index is None:
            return {"error": "City not found"}, 404
        updated_city = request.json
        country['cities'][city_index] = updated_city['name']
        write_json(json_filename, data)
        return updated_city

if __name__ == '__main__':
    app.run(debug=True)
    