import requests
import json
import jsonpath
import logging
import allure
baseUrl = "https://petstore.swagger.io/"


@allure.title("TC-1: Pet API Test - Post")
@allure.description("Inserting a pet")
def test_insert_pet():
    file = open("data/pet.json")
    path = "v2/pet"
    data = json.loads(file.read())
    response = requests.post(url=baseUrl+path, json=data)
    response_json = json.loads(response.text)
    logging.info(f'Insert method is called. Inserted data: {data}')
    logging.info(f'Response: {response.text}')
    assert response.status_code == 200
    assert jsonpath.jsonpath(response_json, '$.id')[0] == data["id"]
    assert jsonpath.jsonpath(response_json, '$.name')[0] == data["name"]


@allure.title("TC-2: Pet API Test - Get")
@allure.description("Retrieving a pet")
def test_get_pet():
    path = "v2/pet/1989"
    response = requests.get(url=baseUrl + path)
    response_json = json.loads(response.text)
    logging.info(f'Get method is called')
    logging.info(f'Response: {response.text}')
    assert response.status_code == 200
    assert jsonpath.jsonpath(response_json, '$.id')[0] == 1989
    assert jsonpath.jsonpath(response_json, '$.name')[0] == "pikachu"


@allure.title("TC-3: Pet API Test - Update")
@allure.description("Updating a pet")
def test_update_pet():
    path = "v2/pet/1989"
    data = {
        'petId': 1989,
        'name': "onix"
    }
    response = requests.post(url=baseUrl + path, data=data)
    logging.info(f'Update method is called')
    logging.info(f'Response: {response.text}')
    assert response.status_code == 200
    response = requests.get(url=baseUrl + path)
    logging.info(f'Get method is called')
    logging.info(f'Response: {response.text}')
    response_json = json.loads(response.text)
    assert jsonpath.jsonpath(response_json, '$.name')[0] == 'onix'


@allure.title("TC-4: Pet API Test - Delete")
@allure.description("Deleting a pet")
def test_delete_pet():
    path = "v2/pet/1989"
    response = requests.delete(url=baseUrl+path)
    logging.info(f'Delete method is called')
    logging.info(f'Response: {response.text}')
    assert response.status_code == 200
    response = requests.get(url=baseUrl + path)
    logging.info(f'Get method is called')
    logging.info(f'Response: {response.text}')
    assert response.status_code == 404



