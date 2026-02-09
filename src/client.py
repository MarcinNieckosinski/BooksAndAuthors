import requests
from typing import Dict, Any


class ApiClient:
    def __init__(self, base_url, headers: Dict[str, str] = None):
        self.base_url = base_url
        self.headers = headers or {}
        self.session = requests.Session()

    def get(self, endpoint: str | None = None, params: Dict[str, Any] = None):
        url = f"{self.base_url}{endpoint}" if endpoint is not None else f"{self.base_url}"
        return self.session.get(url, params=params, headers=self.headers)

    def post(self, endpoint: str | None = None, data: Any = None) -> requests.Response:
        url = f"{self.base_url}{endpoint}" if endpoint is not None else f"{self.base_url}"
        return self.session.post(url, json=data, headers=self.headers)

    def put(self, endpoint: str | None = None, params: Dict[str, Any] = None) -> requests.Response:
        url = f"{self.base_url}{endpoint}" if endpoint is not None else f"{self.base_url}"
        return self.session.put(url, params=params, headers=self.headers)

    def delete(self, endpoint: str | None = None, params: Dict[str, Any] = None) -> requests.Response:
        url = f"{self.base_url}{endpoint}" if endpoint is not None else f"{self.base_url}"
        return self.session.delete(url, params=params, headers=self.headers)
