import requests


class APIClient:

    def get(self, endpoint):

        response = requests.get(endpoint)

        return response