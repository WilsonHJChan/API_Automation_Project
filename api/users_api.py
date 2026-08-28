import requests
import logging

from config import BASE_URL


logging.basicConfig(level=logging.INFO)


def get_user(user_id):

    url = f"{BASE_URL}/users/{user_id}"

    logging.info(f"Sending GET request: {url}")

    response = requests.get(url)

    logging.info(f"Response status: {response.status_code}")

    return response


def create_user(user_data):

    url = f"{BASE_URL}/users"

    logging.info(f"Sending POST request: {url}")

    response = requests.post(url, json=user_data)

    logging.info(f"Response status: {response.status_code}")

    return response


def update_user(user_id, user_data):

    url = f"{BASE_URL}/users/{user_id}"

    logging.info(f"Sending PUT request: {url}")

    response = requests.put(url, json=user_data)

    logging.info(f"Response status: {response.status_code}")

    return response


def delete_user(user_id):

    url = f"{BASE_URL}/users/{user_id}"

    logging.info(f"Sending DELETE request: {url}")

    response = requests.delete(url)

    logging.info(f"Response status: {response.status_code}")

    return response