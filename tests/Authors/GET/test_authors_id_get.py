import pytest


@pytest.mark.authors
@pytest.mark.get
class TestAuthorsGet:
    def test_response_code(self, api_client, authors_data):
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(1))
        assert response.status_code == 200

    def test_response_data(self, api_client, authors_data):
        response_data_object = api_client.get(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(27)).json()
        assert "id" in response_data_object
        assert "idBook" in response_data_object
        assert "firstName" in response_data_object
        assert "lastName" in response_data_object

    def test_response_data_object_elements_types(self, api_client, authors_data):
        response_data_object = api_client.get(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(34)).json()
        assert type(response_data_object["id"]) == int
        assert type(response_data_object["idBook"]) == int
        assert type(response_data_object["firstName"]) == str
        assert type(response_data_object["lastName"]) == str

    def test_existing_id_data(self, api_client, authors_data):
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(45)).json()
        assert response["id"] == authors_data["EXISTING_AUTHOR_ID_DATA"]["id"]
        assert response["firstName"] == authors_data["EXISTING_AUTHOR_ID_DATA"]["firstName"]
        assert response["lastName"] == authors_data["EXISTING_AUTHOR_ID_DATA"]["lastName"]

    def test_zero_id(self, api_client, authors_data):
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(0))
        assert response.status_code == 404

    def test_under_zero_id(self, api_client, authors_data):
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(-1))
        assert response.status_code == 404

    def test_non_existing_id(self, api_client, authors_data):
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(120312))
        assert response.status_code == 404

    def test_not_int_id(self, api_client, authors_data):
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS_ID"].format("A"))
        assert response.status_code == 400
