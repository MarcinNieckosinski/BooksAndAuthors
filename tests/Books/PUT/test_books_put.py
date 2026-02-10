from src.utils import is_iso_date


class TestBooksPut:
    def test_empty_request_response_code(self, api_client, books_data):
        response = api_client.put(books_data["ENDPOINTS"]["BOOKS_ID"].format(0))
        assert response.status_code == 415

    def test_response_code(self, api_client, books_data):
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS_ID"].format(5))
        data = {
            "id": response.json()["id"],
            "title": response.json()["title"],
            "description": response.json()["description"],
            "pageCount": response.json()["pageCount"],
            "excerpt": response.json()["excerpt"],
            "publishDate": response.json()["publishDate"]
        }
        response = api_client.put(books_data["ENDPOINTS"]["BOOKS_ID"].format(5), data=data)
        assert response.json()["id"] == data["id"]
        assert response.json()["title"] == data["title"]
        assert response.json()["description"] == data["description"]
        assert response.json()["pageCount"] == data["pageCount"]
        assert response.json()["excerpt"] == data["excerpt"]
        assert response.json()["publishDate"] == data["publishDate"]

    def test_response_two_books_bad_data(self, api_client, books_data):
        book_one = api_client.get(books_data["ENDPOINTS"]["BOOKS_ID"].format(5))
        book_two = api_client.get(books_data["ENDPOINTS"]["BOOKS_ID"].format(6))
        data = {
            "Book1": {
                "id": book_one.json()["id"],
                "title": book_one.json()["title"],
                "description": book_one.json()["description"],
                "pageCount": book_one.json()["pageCount"],
                "excerpt": book_one.json()["excerpt"],
                "publishDate": book_one.json()["publishDate"]
            },
            "Book2": {
                "id": book_two.json()["id"],
                "title": book_two.json()["title"],
                "description": book_two.json()["description"],
                "pageCount": book_two.json()["pageCount"],
                "excerpt": book_two.json()["excerpt"],
                "publishDate": book_two.json()["publishDate"]
            }
        }
        response = api_client.put(books_data["ENDPOINTS"]["BOOKS_ID"].format(5), data=data)
        assert response.status_code == 200
        assert response.json()["id"] == 0
        assert response.json()["title"] is None
        assert response.json()["description"] is None
        assert response.json()["pageCount"] == 0
        assert response.json()["excerpt"] is None
        assert is_iso_date(response.json()["publishDate"])

    def test_zero_id(self, api_client, books_data):
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS_ID"].format(5))
        data = {
            "id": 0,
            "title": response.json()["title"],
            "description": response.json()["description"],
            "pageCount": response.json()["pageCount"],
            "excerpt": response.json()["excerpt"],
            "publishDate": response.json()["publishDate"]
        }
        response = api_client.put(books_data["ENDPOINTS"]["BOOKS_ID"].format(1), data=data)
        assert response.status_code == 200
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS_ID"].format(0))
        assert response.status_code == 200

    def test_zero_page_count(self, api_client, books_data):
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS_ID"].format(5))
        data = {
            "id": response.json()["id"],
            "title": response.json()["title"],
            "description": response.json()["description"],
            "pageCount": 0,
            "excerpt": response.json()["excerpt"],
            "publishDate": response.json()["publishDate"]
        }
        response = api_client.put(books_data["ENDPOINTS"]["BOOKS_ID"].format(5), data=data)
        assert response.status_code == 200
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS_ID"].format(5))
        assert response.status_code == 200
        assert response.json()["pageCount"] == 0

    def test_empty_data_object(self, api_client, books_data):
        data = {}
        response = api_client.put(books_data["ENDPOINTS"]["BOOKS_ID"].format(5), data=data)
        assert response.status_code == 200

    def test_empty_data_values(self, api_client, books_data):
        data = {
            "id": 0,
            "title": "",
            "description": "",
            "pageCount": 0,
            "excerpt": "",
            "publishDate": ""
        }
        response = api_client.put(books_data["ENDPOINTS"]["BOOKS_ID"].format(5), data=data)
        assert response.status_code == 200
        assert response.json()["id"] == 0
        assert response.json()["title"] is None
        assert response.json()["description"] is None
        assert response.json()["pageCount"] == 0
        assert response.json()["excerpt"] is None
        assert is_iso_date(response.json()["publishDate"])
