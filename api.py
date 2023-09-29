import json
import requests


class PetDemo:
    """API библиотека к веб приложению PetDemo"""

    def __init__(self):
        self.base_url = "http://91.210.171.73:8080/"

    """Token"""

    def post_api_token(self) -> json:
        """Метод (постит) на сервер пользователя и возвращает статус запроса и результат в формате
        JSON с уникальным ключем пользователя"""

        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        data = {
            "username": "admin",
            "password": "admin"
        }

        res = requests.post(self.base_url + 'api/token/auth/', headers=headers, data=json.dumps(data))
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    """Pet Categories"""

    def get_list_of_pet_categories(self, result_limit: int = 10, index_offset: int = 1) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со списком всех категорий животных, limit и offset опциональные параметры"""

        headers = {
            'Authorization': 'Basic YWRtaW46YWRtaW4=',
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        filter = {
            'limit': result_limit,
            'offset': index_offset,
        }
        res = requests.get(self.base_url + 'api/category/', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pet_category(self, pet_category: str, ) -> json:
        """Метод отправляет (постит) на сервер названием новой категорией животного и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленной категории"""
        headers = {
            'Authorization': 'Basic YWRtaW46YWRtaW4=',
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        data = {
            'name': pet_category
        }

        res = requests.post(self.base_url + 'api/category/', headers=headers, data=json.dumps(data))
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_category_by_petid(self, pet_id: str) -> json:
        """Метод делает запрос к API сервера и возвращает категорию животного
        по указанному id и результат в формате JSON"""
        headers = {
            'Authorization': 'Basic YWRtaW46YWRtaW4=',
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        res = requests.get(f'{self.base_url}api/category/{pet_id}/', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def put_category_by_petid(self, pet_id: str, new_pet_category: str) -> json:
        """Метод обновляет название категории животного по указанному id и возвращает результат в формате JSON"""

        headers = {
            'Authorization': 'Basic YWRtaW46YWRtaW4=',
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        data = {
            'name': new_pet_category
        }

        res = requests.put(f'{self.base_url}api/category/{pet_id}/', headers=headers, data=json.dumps(data))
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def del_category_by_petid(self, pet_id: str) -> json:
        """Метод удаляет категорию животного по указанному id и возвращает статус"""
        headers = {
            'Authorization': 'Basic YWRtaW46YWRtaW4=',
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        res = requests.delete(f'{self.base_url}api/category/{pet_id}/', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    """Pets"""

    def get_list_of_pets(self, result_limit: int = 10, index_offset: int = 1) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON
        со списком всех животных, limit и offset опциональные параметры"""

        headers = {
            'Authorization': 'Basic YWRtaW46YWRtaW4=',
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        filter = {
            'limit': result_limit,
            'offset': index_offset,
        }
        res = requests.get(self.base_url + 'api/pet/', headers=headers, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def add_new_pets(self, pets: dict) -> json:
        """Метод отправляет (постит) на сервер названием нового животного и возвращает статус
        запроса на сервер и результат в формате JSON с данными добавленного питомца
        Если категория не найдена приходит ответ 404."""
        headers = {
            'Authorization': 'Basic YWRtaW46YWRtaW4=',
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        res = requests.post(self.base_url + 'api/pet/', headers=headers, data=json.dumps(pets))
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def get_pet_by_id(self, pet_id: str) -> json:
        """Метод делает запрос к API сервера и возвращает животное
        по указанному id и результат в формате JSON"""

        headers = {
            'Authorization': 'Basic YWRtaW46YWRtaW4=',
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        res = requests.get(f'{self.base_url}api/pet/{pet_id}/', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def put_pet_by_id(self, pet_id: str, new_pets: dict) -> json:
        """Метод обновляет название данные животного по указанному id и возвращает результат в формате JSON"""

        headers = {
            'Authorization': 'Basic YWRtaW46YWRtaW4=',
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        res = requests.put(f'{self.base_url}api/pet/{pet_id}/', headers=headers, data=json.dumps(new_pets))
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result

    def del_pet_by_id(self, pet_id: str) -> json:
        """Метод удаляет животного по указанному id и возвращает статус"""
        headers = {
            'Authorization': 'Basic YWRtaW46YWRtaW4=',
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        res = requests.delete(f'{self.base_url}api/pet/{pet_id}/', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
