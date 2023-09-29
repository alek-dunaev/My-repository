from api import PetDemo

pd = PetDemo()


def test_post_api_token():
    """ Проверяем что запрос api токена возвращает статус 200 и в результате содержится слово token"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = (pd.post_api_token())

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'token' in result


"""Pet Categories"""


def test_get_list_of_pet_categories(result_limit: int = 100, index_offset: int = 0):
    """ Проверяем что запрос всех категорий животных возвращает не пустой список.
    Запрашиваеем список всех животных и проверяем что список не пустой.
    Доступное значение параметров limit(Number of results to return per page) и offset(The initial index from which
    to return the results.) """

    status, result = pd.get_list_of_pet_categories(result_limit, index_offset)
    result = result['results']

    assert status == 200
    assert len(result) > 0


def test_add_new_pet_category(pet_category="hyenas"):
    """Проверяем что можно добавить уникальную категорию животного с корректными данными"""

    # Добавляем питомца
    status, result = pd.add_new_pet_category(pet_category)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 201
    assert result['name'] == pet_category


def test_get_category_by_petid(pet_id="237"):
    """Проверяем получение категории животного по petid"""

    status, result = pd.get_category_by_petid(pet_id)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == 'Cats'


def test_put_category_by_petid(pet_id="261", new_pet_category="parrott"):
    """Проверяем внесение изменений в категорию животного по petid"""

    status, result = pd.put_category_by_petid(pet_id, new_pet_category)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == 'parrott'


def test_successful_del_pet_category(pet_category="hares"):
    """Проверяем возможность удаления питомца"""

    # Создаём новую категорию
    status, result = pd.add_new_pet_category(pet_category)

    # Сверяем полученный ответ с ожидаемым результатом
    assert result['name'] == pet_category

    if status == 201:
        # Удаляем новую категорию
        status, result = pd.del_category_by_petid(result['id'])
        print(result)
        assert status == 204
    else:
        print("Новая категория не создана")

    """Pets"""


def test_get_list_of_pets(result_limit: int = 100, index_offset: int = 0):
    """ Проверяем что запрос всех животных возвращает не пустой список.
    Запрашиваеем список всех животных и проверяем что список не пустой.
    Доступное значение параметров limit(Number of results to return per page) и offset(The initial index from which
    to return the results.) """

    status, result = pd.get_list_of_pets(result_limit, index_offset)
    result = result['results']

    assert status == 200
    assert len(result) > 0


def test_add_new_pets(pets={"name": "Barsik",
                            "photo_url": "WWW.Photo.Com",
                            "category": {
                                "name": "cats"
                            },
                            "status": "available"
                            }):
    """Проверяем что можно добавить животное с корректными данными"""

    # Добавляем питомца
    status, result = pd.add_new_pets(pets)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 201
    assert result['name'] == pets['name']


def test_get_pet_by_id(pet_id="118"):
    """Проверяем получение животного по petid"""

    status, result = pd.get_pet_by_id(pet_id)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == 'Bob'


def test_put_pet_by_id(pet_id="120", new_pet={"name": "Murzik",
                                              "photo_url": "WWW.Photo2.Com",
                                              "category": {
                                                  "name": "cats"
                                              },
                                              "status": "available"
                                              }):
    """Проверяем внесение изменений в данные животного по petid"""

    status, result = pd.put_pet_by_id(pet_id, new_pet)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == 'Murzik'


def test_successful_del_pet_by_id(new_pet={"name": "Kuzya",
                                           "photo_url": "WWW.Photo.Com",
                                           "category": {
                                               "name": "cats"
                                           },
                                           "status": "available"
                                           }):
    """Проверяем возможность удаления питомца"""

    # Создаём новое животное
    status, result = pd.add_new_pets(new_pet)

    # Сверяем полученный ответ с ожидаемым результатом
    assert result['name'] == new_pet['name']

    if status == 201:
        # Удаляем новое животное
        status, result = pd.del_pet_by_id(result['id'])
        print(result)
        assert status == 204
    else:
        print("Новое животное не создано")
