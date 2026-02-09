import json
import pytest
from src.client import ApiClient


@pytest.fixture
def api_client(base_url="https://fakerestapi.azurewebsites.net/api/v1/") -> ApiClient:
    return ApiClient(base_url=base_url)

@pytest.fixture
def authors_data():
    with open('../../../data/Authors/authors_data.json') as data_file:
        data = json.load(data_file)

    return data