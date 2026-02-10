import pytest


@pytest.mark.authors
@pytest.mark.delete
class TestAuthorsDelete:
    def test_response_code(self, api_client, authors_data):
        response = api_client.delete(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(1))
        assert response.status_code == 200

    def test_response_data(self, api_client, authors_data):
        response = api_client.delete(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(27))
        assert response.text == ""

    def test_zero_id(self, api_client, authors_data):
        response = api_client.delete(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(0))
        assert response.status_code == 404

    def test_under_zero_id(self, api_client, authors_data):
        response = api_client.delete(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(-1))
        assert response.status_code == 404

    def test_non_existing_id(self, api_client, authors_data):
        response = api_client.delete(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(120312))
        assert response.status_code == 404

    def test_not_int_id(self, api_client, authors_data):
        response = api_client.delete(authors_data["ENDPOINTS"]["AUTHORS_ID"].format("A"))
        assert response.status_code == 400
