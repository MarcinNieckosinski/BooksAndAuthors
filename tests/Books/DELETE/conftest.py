import json
from pathlib import Path
import pytest
from src.client import ApiClient


@pytest.fixture
def api_client(base_url="https://fakerestapi.azurewebsites.net/api/v1/") -> ApiClient:
    return ApiClient(base_url=base_url)

@pytest.fixture
def books_data(pytestconfig):
    path = Path(__file__).resolve()
    root = ''
    for parent in [path] + list(path.parents):
        if (parent / ".git").exists():
            root = parent
            break
        if (parent / ".lock").exists():
            root = parent
            break
    file_path = root / "data\\Books\\books_data.json"
    data = json.loads(file_path.read_text())

    return data