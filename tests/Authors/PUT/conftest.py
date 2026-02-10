import json
import pytest
from src.client import ApiClient


@pytest.fixture
def api_client(base_url="https://fakerestapi.azurewebsites.net/api/v1/") -> ApiClient:
    return ApiClient(base_url=base_url)

@pytest.fixture
def authors_data(pytestconfig):
    root = pytestconfig.rootpath
    file_path = root / "..\\data\\Authors\\authors_data.json"
    data = json.loads(file_path.read_text())

    return data