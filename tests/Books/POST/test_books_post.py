from src.utils import is_iso_date


class TestBooksPost:
    def test_empty_request_response_code(self, api_client, books_data):
        response = api_client.post(books_data["ENDPOINTS"]["BOOKS"])
        assert response.status_code == 415

    def test_response_code(self, api_client, books_data):
        data = {
            "id": 1344,
            "title": "Of QAs and Men",
            "description": "How devs fought QA and lost",
            "pageCount": 420,
            "excerpt": "Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.\n",
            "publishDate": "2026-02-10T10:23:51.793Z"
        }
        response = api_client.post(books_data["ENDPOINTS"]["BOOKS"], data=data)
        assert response.status_code == 200

    def test_response_two_books_bad_data(self, api_client, books_data):
        data = { "Book1": {
            "id": 1344,
            "title": "Of QAs and Men",
            "description": "How devs fought QA and lost",
            "pageCount": 420,
            "excerpt": "Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.\n",
            "publishDate": "2026-02-10T10:23:51.793Z"
        },
            "Book2": {
            "id": 1344,
            "title": "Of QAs and Men",
            "description": "How devs fought QA and lost",
            "pageCount": 420,
            "excerpt": "Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.\n",
            "publishDate": "2026-02-10T10:23:51.793Z"
        }
        }
        response = api_client.post(books_data["ENDPOINTS"]["BOOKS"], data=data)
        response_data_object = response.json()
        assert response_data_object["id"] == 0
        assert response_data_object["title"] is None
        assert response_data_object["description"] is None
        assert response_data_object["pageCount"] == 0
        assert response_data_object["excerpt"] is None
        assert is_iso_date(response_data_object["publishDate"])

    def test_zero_id(self, api_client, books_data):
        data = {
            "id": 0,
            "title": "Of QAs and Men",
            "description": "How devs fought QA and lost",
            "pageCount": 420,
            "excerpt": "Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.\n",
            "publishDate": "2026-02-10T10:23:51.793Z"
        }
        response = api_client.post(books_data["ENDPOINTS"]["BOOKS"], data=data)
        assert response.status_code == 200
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS_ID"].format(0))
        assert response.status_code == 200

    def test_zero_page_count(self, api_client, books_data):
        data = {
            "id": 1344,
            "title": "Of QAs and Men",
            "description": "How devs fought QA and lost",
            "pageCount": 0,
            "excerpt": "Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem."
                       "\nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.\n",
            "publishDate": "2026-02-10T10:23:51.793Z"
        }
        response = api_client.post(books_data["ENDPOINTS"]["BOOKS"], data=data)
        assert response.status_code == 200
        response = api_client.get(books_data["ENDPOINTS"]["BOOKS_ID"].format(1344))
        assert response.status_code == 200
        assert response.json()["pageCount"] == 0

    def test_empty_data_object(self, api_client, books_data):
        data = {}
        response = api_client.post(books_data["ENDPOINTS"]["BOOKS"], data=data)
        response_data_object = response.json()
        assert response.status_code == 200
        assert response_data_object["id"] == 0
        assert response_data_object["title"] is None
        assert response_data_object["description"] is None
        assert response_data_object["pageCount"] == 0
        assert response_data_object["excerpt"] is None
        assert is_iso_date(response_data_object["publishDate"])

    def test_empty_data_values(self, api_client, books_data):
        data = {
            "id": 0,
            "title": "",
            "description": "",
            "pageCount": 0,
            "excerpt": "",
            "publishDate": ""
        }
        response = api_client.post(books_data["ENDPOINTS"]["BOOKS"], data=data)
        response_data_object = response.json()
        assert response.status_code == 200
        assert response_data_object["id"] == 0
        assert response_data_object["title"] is None
        assert response_data_object["description"] is None
        assert response_data_object["pageCount"] == 0
        assert response_data_object["excerpt"] is None
        assert is_iso_date(response_data_object["publishDate"])
