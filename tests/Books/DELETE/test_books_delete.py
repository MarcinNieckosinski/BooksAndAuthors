class TestBooksDelete:
    def test_response_code(self, api_client, books_data):
        response = api_client.delete(books_data["ENDPOINTS"]["BOOKS_ID"].format(12))
        assert response.status_code == 200

    def test_response_data(self, api_client, books_data):
        response = api_client.delete(books_data["ENDPOINTS"]["BOOKS_ID"].format(33))
        assert response.text == ""

    def test_zero_id(self, api_client, books_data):
        response = api_client.delete(books_data["ENDPOINTS"]["BOOKS_ID"].format(0))
        assert response.status_code == 404

    def test_under_zero_id(self, api_client, books_data):
        response = api_client.delete(books_data["ENDPOINTS"]["BOOKS_ID"].format(-5))
        assert response.status_code == 404

    def test_non_existing_id(self, api_client, books_data):
        response = api_client.delete(books_data["ENDPOINTS"]["BOOKS_ID"].format(11166732))
        assert response.status_code == 404

    def test_not_int_id(self, api_client, books_data):
        response = api_client.delete(books_data["ENDPOINTS"]["BOOKS_ID"].format("C"))
        assert response.status_code == 400
