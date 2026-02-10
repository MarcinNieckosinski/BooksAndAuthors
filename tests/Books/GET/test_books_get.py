from src.utils import is_iso_date


class TestBooksGet:
    def test_response_code(self, api_client, books_data):
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS"])
        assert response.status_code == 200

    def test_response_data_not_empty(self, api_client, books_data):
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS"])
        response_data = response.json()
        assert len(response_data) != 0

    def test_response_data_single_object_structure(self, api_client, books_data):
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS"])
        response_data_object = response.json()[0]
        assert "id" in response_data_object
        assert "title" in response_data_object
        assert "description" in response_data_object
        assert "pageCount" in response_data_object
        assert "excerpt" in response_data_object
        assert "publishDate" in response_data_object

    def test_response_data_object_elements_types(self, api_client, books_data):
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS"])
        response_data_object = response.json()[0]
        assert type(response_data_object["id"]) == int
        assert type(response_data_object["title"]) == str
        assert type(response_data_object["description"]) == str
        assert type(response_data_object["pageCount"]) == int
        assert type(response_data_object["excerpt"]) == str
        assert is_iso_date(response_data_object["publishDate"])

    def test_unique_ids(self, api_client, books_data):
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS"])
        response_data = response.json()
        data_ids = [obj["id"] for obj in response_data]
        assert len(set(data_ids)) == len(response_data)
