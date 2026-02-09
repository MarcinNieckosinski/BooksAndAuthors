class TestAuthorsByBookIdGet:
    endpoint = "Authors/authors/books/{}"

    def test_response_code(self, api_client):
        response = api_client.get(self.endpoint.format(1))
        assert response.status_code == 200

    def test_response_data(self, api_client):
        response_data_object = api_client.get(self.endpoint.format(27)).json()
        assert type(response_data_object) == list
        assert "id" in response_data_object[0]
        assert "idBook" in response_data_object[0]
        assert "firstName" in response_data_object[0]
        assert "lastName" in response_data_object[0]

    def test_response_data_object_elements_types(self, api_client):
        response_data_object = api_client.get(self.endpoint.format(34)).json()[1]
        assert type(response_data_object["id"]) == int
        assert type(response_data_object["idBook"]) == int
        assert type(response_data_object["firstName"]) == str
        assert type(response_data_object["lastName"]) == str


    def test_zero_id(self, api_client):
        response = api_client.get(self.endpoint.format(0))
        assert response.status_code == 200
        assert response.json() == []

    def test_non_existing_id(self, api_client):
        response = api_client.get(self.endpoint.format(120312))
        assert response.status_code == 200
        assert response.json() == []

    def test_under_zero_id(self, api_client):
        response = api_client.get(self.endpoint.format(-1))
        assert response.status_code == 200
        assert response.json() == []

    def test_not_int_id(self, api_client):
        response = api_client.get(self.endpoint.format("A"))
        assert response.status_code == 400

    def test_authors_belong_to_book(self, api_client):
        response = api_client.get(self.endpoint.format(2))
        for author in response.json():
            author_id = author["id"]
            author_endpoint = self.endpoint.replace("authors/books/", "").format(author_id)
            author_response = api_client.get(author_endpoint)
            assert author_response.json()["idBook"] == 2
