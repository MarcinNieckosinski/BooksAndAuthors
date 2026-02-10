class TestAuthorsPost:
    def test_empty_request_response_code(self, api_client, authors_data):
        response = api_client.put(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(0))
        assert response.status_code == 415

    def test_response_code(self, api_client, authors_data):
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(5))
        data = {
            "id": response.json()["id"],
            "idBook": response.json()["idBook"],
            "firstName": response.json()["firstName"],
            "lastName": response.json()["lastName"]
        }
        response = api_client.put(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(5), data=data)
        assert response.json()["id"] == data["id"]
        assert response.json()["idBook"] == data["idBook"]
        assert response.json()["firstName"] == data["firstName"]
        assert response.json()["lastName"] == data["lastName"]

    def test_response_two_authors_bad_data(self, api_client, authors_data):
        author_one = api_client.get(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(5))
        author_two = api_client.get(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(6))
        data = { "author_one": {
            "id": author_one.json()["id"],
            "idBook": author_one.json()["idBook"],
            "firstName": author_one.json()["firstName"],
            "lastName": author_one.json()["lastName"]
        },
            "author_two": {
                "id": author_two.json()["id"],
                "idBook": author_two.json()["idBook"],
                "firstName": author_two.json()["firstName"],
                "lastName": author_two.json()["lastName"]
            }
        }
        response = api_client.put(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(5), data=data)
        assert response.status_code == 200
        assert response.json()["id"] == 0
        assert response.json()["idBook"] == 0
        assert response.json()["firstName"] is None
        assert response.json()["lastName"] is None

    def test_zero_id(self, api_client, authors_data):
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(5))
        data = {
            "id": 0,
            "idBook": response.json()["idBook"],
            "firstName": response.json()["firstName"],
            "lastName": response.json()["lastName"]
        }
        response = api_client.put(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(1), data=data)
        assert response.status_code == 200
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(0))
        assert response.status_code == 200

    def test_zero_book_id(self, api_client, authors_data):
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(5))
        data = {
            "id": response.json()["id"],
            "idBook": 0,
            "firstName": response.json()["firstName"],
            "lastName": response.json()["lastName"]
        }
        response = api_client.put(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(5), data=data)
        assert response.status_code == 200
        response = api_client.get(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(5))
        assert response.status_code == 200
        assert response.json()["idBook"] == 0

    def test_empty_data_object(self, api_client, authors_data):
        data = {}
        response = api_client.put(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(5), data=data)
        assert response.status_code == 200

    def test_empty_data_values(self, api_client, authors_data):
        data = {
            "id": 0,
            "idBook": 0,
            "firstName": "",
            "lastName": ""
        }
        response = api_client.put(authors_data["ENDPOINTS"]["AUTHORS_ID"].format(5), data=data)
        assert response.status_code == 200
        assert response.json()["id"] == 0
        assert response.json()["idBook"] == 0
        assert response.json()["firstName"] == ''
        assert response.json()["lastName"] == ''
