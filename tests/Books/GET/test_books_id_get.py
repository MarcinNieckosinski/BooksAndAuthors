from src.utils import is_iso_date
import pytest


@pytest.mark.books
@pytest.mark.get
class TestBooksIdGet:
    def test_response_code(self, api_client, books_data):
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS_ID"].format(11))
        assert response.status_code == 200

    def test_response_data(self, api_client, books_data):
        response_data_object = api_client.get(books_data["ENDPOINTS"]["BOOKS_ID"].format(134)).json()
        assert "id" in response_data_object
        assert "title" in response_data_object
        assert "description" in response_data_object
        assert "pageCount" in response_data_object
        assert "excerpt" in response_data_object
        assert "publishDate" in response_data_object

    def test_response_data_object_elements_types(self, api_client, books_data):
        response_data_object = api_client.get(books_data["ENDPOINTS"]["BOOKS_ID"].format(55)).json()
        assert type(response_data_object["id"]) == int
        assert type(response_data_object["title"]) == str
        assert type(response_data_object["description"]) == str
        assert type(response_data_object["pageCount"]) == int
        assert type(response_data_object["excerpt"]) == str
        assert is_iso_date(response_data_object["publishDate"])

    def test_existing_id_data(self, api_client, books_data):
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS_ID"].format(67)).json()
        assert response["id"] == books_data["EXISTING_BOOK_DATA"]["id"]
        assert response["title"] == books_data["EXISTING_BOOK_DATA"]["title"]
        assert response["description"] == books_data["EXISTING_BOOK_DATA"]["description"]
        assert response["pageCount"] == books_data["EXISTING_BOOK_DATA"]["pageCount"]
        assert response["excerpt"] == books_data["EXISTING_BOOK_DATA"]["excerpt"]
        assert response["publishDate"] == books_data["EXISTING_BOOK_DATA"]["publishDate"]

    def test_zero_id(self, api_client, books_data):
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS_ID"].format(0))
        assert response.status_code == 404

    def test_under_zero_id(self, api_client, books_data):
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS_ID"].format(-11))
        assert response.status_code == 404

    def test_non_existing_id(self, api_client, books_data):
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS_ID"].format(999999999))
        assert response.status_code == 404

    def test_not_int_id(self, api_client, books_data):
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS_ID"].format("Q"))
        assert response.status_code == 400
