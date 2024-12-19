import requests

BASE_URL = "http://localhost:5000/data"

def test_list_continents():
    response = requests.get(f"{BASE_URL}/continents")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_continent():
    new_continent = {"name": "Europe", "countries": []}
    response = requests.post(f"{BASE_URL}/continents", json=new_continent)
    assert response.status_code == 201
    assert response.json()["name"] == "Europe"

def test_get_continent():
    response = requests.get(f"{BASE_URL}/continents/Europe")
    assert response.status_code == 200
    assert response.json()["name"] == "Europe"

def test_update_continent():
    updated_continent = {"name": "Europe", "countries": [{"name": "France", "cities": ["Paris"]}]}
    response = requests.put(f"{BASE_URL}/continents/Europe", json=updated_continent)
    assert response.status_code == 200
    assert response.json()["countries"][0]["name"] == "France"

def test_delete_continent():
    response = requests.delete(f"{BASE_URL}/continents/Europe")
    assert response.status_code == 204

def test_create_country():
    new_country = {"name": "Kenya", "cities": ["Nairobi", "Mombasa"]}
    response = requests.post(f"{BASE_URL}/continents/Africa/countries", json=new_country)
    assert response.status_code == 201
    assert response.json()["name"] == "Kenya"

def test_get_country():
    response = requests.get(f"{BASE_URL}/continents/Africa/countries/Kenya")
    assert response.status_code == 200
    assert response.json()["name"] == "Kenya"

def test_update_country():
    updated_country = {"name": "Kenya", "cities": ["Nairobi", "Mombasa", "Kisumu"]}
    response = requests.put(f"{BASE_URL}/continents/Africa/countries/Kenya", json=updated_country)
    assert response.status_code == 200
    assert response.json()["cities"] == ["Nairobi", "Mombasa", "Kisumu"]

def test_delete_country():
    response = requests.delete(f"{BASE_URL}/continents/Africa/countries/Kenya")
    assert response.status_code == 204

def test_create_city():
    new_city = {"name": "Ibadan"}
    response = requests.post(f"{BASE_URL}/continents/Africa/countries/Nigeria/cities", json=new_city)
    assert response.status_code == 201
    assert response.json()["name"] == "Ibadan"

def test_list_cities():
    response = requests.get(f"{BASE_URL}/continents/Africa/countries/Nigeria/cities")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_city():
    response = requests.get(f"{BASE_URL}/continents/Africa/countries/Nigeria/cities/Ibadan")
    assert response.status_code == 200
    assert response.json()["name"] == "Ibadan"

def test_update_city():
    updated_city = {"name": "Ibadan"}
    response = requests.put(f"{BASE_URL}/continents/Africa/countries/Nigeria/cities/Ibadan", json=updated_city)
    assert response.status_code == 200
    assert response.json()["name"] == "Ibadan"

def test_delete_city():
    response = requests.delete(f"{BASE_URL}/continents/Africa/countries/Nigeria/cities/Ibadan")
    assert response.status_code == 204

def test_get_country_continent():
    response = requests.get(f"{BASE_URL}/countries/Nigeria/continent")
    assert response.status_code == 200
    assert response.json()["continent"] == "Africa"
