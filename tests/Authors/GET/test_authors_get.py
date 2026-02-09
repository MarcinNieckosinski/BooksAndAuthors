class TestAuthorsGet:
    def test_response_code(self, api_client, authors_data):
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS"])
        assert response.status_code == 200

    def test_response_data_not_empty(self, api_client, authors_data):
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS"])
        response_data = response.json()
        assert len(response_data) != 0

    def test_response_data_single_object_structure(self, api_client, authors_data):
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS"])
        response_data_object = response.json()[0]
        assert "id" in response_data_object
        assert "idBook" in response_data_object
        assert "firstName" in response_data_object
        assert "lastName" in response_data_object

    def test_response_data_object_elements_types(self, api_client, authors_data):
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS"])
        response_data_object = response.json()[0]
        assert type(response_data_object["id"]) == int
        assert type(response_data_object["idBook"]) == int
        assert type(response_data_object["firstName"]) == str
        assert type(response_data_object["lastName"]) == str

    def test_unique_ids(self, api_client, authors_data):
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS"])
        response_data = response.json()
        data_ids = [obj["id"] for obj in response_data]
        assert len(set(data_ids)) == len(response_data)
