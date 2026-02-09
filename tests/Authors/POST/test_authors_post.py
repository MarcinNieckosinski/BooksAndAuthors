class TestAuthorsPost:
    def test_empty_request_response_code(self, api_client, authors_data):
        response = api_client.post(authors_data["ENDPOINTS"]["AUTHORS"])
        assert response.status_code == 415

    def test_response_code(self, api_client, authors_data):
        data = {
            "id": 1275,
            "idBook": 1299,
            "firstName": "firstname 1275",
            "lastName": "lastname 1275"
        }
        response = api_client.post(authors_data["ENDPOINTS"]["AUTHORS"], data=data)
        assert response.status_code == 200

    def test_response_two_authors(self, api_client, authors_data):
        data = { "Author1275": {
            "id": 1275,
            "idBook": 1299,
            "firstName": "firstname 1275",
            "lastName": "lastname 1275"
        },
            "Author1276": {
                "id": 1276,
                "idBook": 1292,
                "firstName": "firstname 1276",
                "lastName": "lastname 1276"
            }
        }
        response = api_client.post(authors_data["ENDPOINTS"]["AUTHORS"], data=data)
        assert response.status_code == 200
        assert response.json()["id"] == 0
        assert response.json()["idBook"] == 0
        assert response.json()["firstName"] is None
        assert response.json()["lastName"] is None

    def test_zero_id(self, api_client, authors_data):
        data = {
            "id": 0,
            "idBook": 1299,
            "firstName": "firstname 1275",
            "lastName": "lastname 1275"
        }
        response = api_client.post(authors_data["ENDPOINTS"]["AUTHORS"], data=data)
        assert response.status_code == 200
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(0))
        assert response.status_code == 200

    def test_zero_book_id(self, api_client, authors_data):
        data = {
            "id": 1270,
            "idBook": 0,
            "firstName": "firstname 1270",
            "lastName": "lastname 1270"
        }
        response = api_client.post(authors_data["ENDPOINTS"]["AUTHORS"], data=data)
        assert response.status_code == 200
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(1270))
        assert response.status_code == 200
        assert response.json()["idBook"] == 0

    def test_empty_data_object(self, api_client, authors_data):
        data = {}
        response = api_client.post(authors_data["ENDPOINTS"]["AUTHORS"], data=data)
        assert response.status_code == 200
        assert response.json()["id"] == 0
        assert response.json()["idBook"] == 0
        assert response.json()["firstName"] is None
        assert response.json()["lastName"] is None

    def test_empty_data_values(self, api_client, authors_data):
        data = {
            "id": 0,
            "idBook": 0,
            "firstName": "",
            "lastName": ""
        }
        response = api_client.post(authors_data["ENDPOINTS"]["AUTHORS"], data=data)
        assert response.status_code == 200
        assert response.json()["id"] == 0
        assert response.json()["idBook"] == 0
        assert response.json()["firstName"] == ''
        assert response.json()["lastName"] == ''
