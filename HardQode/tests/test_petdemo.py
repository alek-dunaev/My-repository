from api import PetDemo
import pytest
import random
import string

pd = PetDemo()


@pytest.fixture()
def get_some_category_petid():
    category = generate_letters_string(10)

    status, result = pd.add_new_pet_category(category)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 201
    return result


@pytest.fixture()
def get_some_petid(get_some_category_petid):
    pets = {"name": generate_letters_string(10),
            "photo_url": generate_letters_string(15),
            "category": {
                "name": get_some_category_petid['name']
            },
            "status": 'available'
            }
    status, result = pd.add_new_pets(pets)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 201
    return result


def generate_string(n):
    return "x" * n


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


# 20 популярных китайских иероглифов
def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


def generate_letters_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


# 1
def test_post_api_token():
    """ Проверяем что запрос api токена возвращает статус 200 и в результате содержится слово token"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = (pd.post_api_token())

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert 'token' in result


"""Pet Categories"""


# 2
@pytest.mark.parametrize('result_limit',
                         [''
                             , '10'
                             , generate_string(256)
                          ],
                         ids=['empty string', '10', '256'])
@pytest.mark.parametrize('index_offset',
                         [''
                             , '10'
                             , generate_string(256)
                          ],
                         ids=['empty string', '10', '256'])
def test_get_list_of_pet_categories_with_valid_data(result_limit, index_offset):
    """Позитивные тесты. Запрашиваем список всех категорий животных и проверяем что список не пустой и статус
    ответа 200. Доступное значение параметров limit(Number of results to return per page) и offset(The initial
    index from which to return the results.) пустая строка; 10; строка = 255 символов"""

    status, result = pd.get_list_of_pet_categories(result_limit, index_offset)
    result = result['results']

    assert status == 200
    assert len(result) > 0


# 3
@pytest.mark.parametrize('result_limit',
                         [generate_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                          ],
                         ids=['more than 1000', 'russian letters', 'upper russian letters ',
                              'chinese_letters', 'special simbols'])
@pytest.mark.parametrize('index_offset',
                         [generate_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                          ],
                         ids=['more than 1000', 'russian letters', 'upper russian letters ',
                              'chinese_letters', 'special simbols'])
def test_get_list_of_pet_categories_with_negative_data(result_limit, index_offset):
    """Негативные тесты. Проверяем что запрос всех категорий животных возвращает статус с ошибкой ожидаем
    400 (Bad Request),а не 500 (Internal Server Error) сервер должен уметь обрабатывать ошибочные запросы. Запрашиваем
    список всех животных c неверными данными. Доступное значение параметров limit(Number of results to return per page)
    и offset(The initial index from which to return the results.) строка длиной > 1000 символов; кодировка (кириллица,
     китайские символы); спецсимволы"""

    status, result = pd.get_list_of_pet_categories(result_limit, index_offset)

    assert status == 400


# 4
@pytest.mark.parametrize('name_category', [generate_letters_string(10)], ids=['unique category'])
def test_add_new_pet_category_with_valid_data(name_category):
    """Позитивные тесты. Проверяем что можно добавить уникальную категорию животного с корректными данными"""

    # Добавляем питомца
    status, result = pd.add_new_pet_category(name_category)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 201
    assert result['name'] == name_category
    # удаляем созданную категорию
    pd.del_category_by_petid(result['id'])


# 5
@pytest.mark.parametrize('name_category',
                         [''
                             , 'cats'
                             , generate_letters_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                             , generate_string(10)
                          ],
                         ids=['empty category', 'not unique', 'more than 1000', 'russian', 'RUSSIAN', 'chinese',
                              'specials', 'digits'])
def test_add_new_pet_category_with_negative_data(name_category):
    """Негативные тесты. Проверяем что сервер возвращает статус 400 при попытке добавить категорию животного
    с некорректными данными.
    Пустая категория, неуникальная категория, категория больше длиной более 1000, на русском языке, большие русские
    буквы, китайские символы, спецсимволы, числа """

    # Добавляем питомца
    status, result = pd.add_new_pet_category(name_category)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400


# 6
def test_get_category_by_petid_with_valid_date(get_some_category_petid):
    """Позитивный тест. Проверяем получение категории животного по корректному petid"""

    status, result = pd.get_category_by_petid(get_some_category_petid['id'])

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == get_some_category_petid['name']


# 7
@pytest.mark.parametrize('pet_id',
                         [''
                             , generate_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                          ],
                         ids=['empty', 'more than 1000', 'russian', 'RUSSIAN', 'chinese', 'special'])
def test_get_category_by_petid_with_negative_date(pet_id):
    """Негативные тест. Проверяем наличие ошибки от сервера при передаче неверного petid
    Пустая строка, id больше 1000, русские буквы, большие русские буквы, китайские символы, спецсимволы."""

    status, result = pd.get_category_by_petid(pet_id)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400


# 8
@pytest.mark.parametrize('pet_id',
                         ['261'],
                         ids=['valid pet_id'])
@pytest.mark.parametrize('new_pet_category',
                         ['parrott'],
                         ids=['valid pet category'])
def test_put_category_by_petid_with_valid_data(pet_id, new_pet_category):
    """Позитивный тест. Проверяем внесение изменений в категорию животного по корректному petid"""

    status, result = pd.put_category_by_petid(pet_id, new_pet_category)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == 'parrott'


# 9
@pytest.mark.parametrize('pet_id',
                         [''
                             , generate_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                             , ],
                         ids=['empty', 'more than 1000', 'russian', 'RUSSIAN', 'chinese', 'special'])
@pytest.mark.parametrize('new_pet_category',
                         [''
                             , 'cats'
                             , generate_letters_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                             , generate_string(10)
                          ],
                         ids=['empty category', 'not unique', 'more than 1000', 'russian', 'RUSSIAN', 'chinese',
                              'specials', 'digits'])
def test_put_category_by_petid_with_negative_data(pet_id, new_pet_category):
    """Негативные тесты. Проверяем внесение изменений в категорию животного по некорректному petid
    и некорректными данными в запросе"""

    status, result = pd.put_category_by_petid(pet_id, new_pet_category)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400


# 10
def test_successful_del_pet_category(pet_category="hares"):
    """Позитивный тест. Проверяем возможность удаления животного"""

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


# 11
@pytest.mark.parametrize('pet_id',
                         [''
                             , generate_letters_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                             , generate_string(10)
                          ],
                         ids=['empty category', 'more than 1000', 'russian', 'RUSSIAN', 'chinese',
                              'specials', 'digits'])
def test_fail_del_pet_category(pet_id):
    """Негативные тесты. Проверяем возможность удаления животного c неверными данными id"""

    status, result = pd.del_category_by_petid(pet_id)

    assert status == 404

    """Pets"""


# 12
@pytest.mark.parametrize('result_limit',
                         [''
                             , '10'
                             , generate_string(256)
                          ],
                         ids=['empty string', '10', '256'])
@pytest.mark.parametrize('index_offset',
                         [''
                             , '10'
                             , generate_string(256)
                          ],
                         ids=['empty string', '10', '256'])
def test_get_list_of_pets_with_valid_data(result_limit, index_offset):
    """Позитивные тесты. Запрашиваем список всех животных и проверяем что список не пустой и статус ответа 200.
    Доступное значение параметров limit(Number of results to return per page) и offset(The initial index from which
    to return the results.) пустая строка; 10; строка = 255 символов"""

    status, result = pd.get_list_of_pets(result_limit, index_offset)
    result = result['results']

    assert status == 200
    assert len(result) > 0


# 13
@pytest.mark.parametrize('result_limit',
                         [generate_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                          ],
                         ids=['more than 1000', 'russian letters', 'upper russian letters ',
                              'chinese_letters', 'special simbols'])
@pytest.mark.parametrize('index_offset',
                         [generate_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                          ],
                         ids=['more than 1000', 'russian letters', 'upper russian letters ',
                              'chinese_letters', 'special simbols'])
def test_get_list_of_pets_with_negative_data(result_limit, index_offset):
    """Негативные тесты. Проверяем что запрос всех животных возвращает статус с ошибкой ожидаем 400 (Bad Request),
    а не 500 (Internal Server Error) сервер должен уметь обрабатывать ошибочные запросы. Запрашиваем
    список всех животных c неверными данными. Доступное значение параметров limit(Number of results to return per page)
     и offset(The initial index from which to return the results.)
   строка длиной > 1000 символов; кодировка (кириллица, китайские символы); спецсимволы"""

    status, result = pd.get_list_of_pets(result_limit, index_offset)

    assert status == 400


# 14
@pytest.mark.parametrize('pets',
                         [{"name": "Barsik",
                           "photo_url": "WWW.Photo.Com",
                           "category": {
                               "name": "cats"
                           },
                           "status": "available"
                           }],
                         ids=['good pet'])
def test_add_new_pets_with_valid_data(pets):
    """Позитивные тесты. Проверяем что можно добавить животное с корректными данными"""

    # Добавляем питомца
    status, result = pd.add_new_pets(pets)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 201
    assert result['name'] == pets['name']


# 15
@pytest.mark.parametrize('name',
                         [''
                             , generate_letters_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                             , generate_string(10)
                          ],
                         ids=['empty name', 'more than 1000', 'russian', 'RUSSIAN', 'chinese',
                              'specials', 'digits'])
@pytest.mark.parametrize('photo_url',
                         [''
                             , generate_letters_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                             , generate_string(10)
                          ],
                         ids=['empty name', 'more than 1000', 'russian', 'RUSSIAN', 'chinese',
                              'specials', 'digits'])
@pytest.mark.parametrize('category_name',
                         [''
                             , generate_letters_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                             , generate_string(10)
                          ],
                         ids=['empty name', 'more than 1000', 'russian', 'RUSSIAN', 'chinese',
                              'specials', 'digits'])
@pytest.mark.parametrize('status',
                         [''
                             , generate_letters_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                             , generate_string(10)
                          ],
                         ids=['empty name', 'more than 1000', 'russian', 'RUSSIAN', 'chinese',
                              'specials', 'digits'])
def test_add_new_pets_with_negative_data(name, photo_url, category_name, status):
    """Негативные тесты. Проверяем что получим статус ошибки при попытке добавить животное с некорректными данными"""
    pets = {"name": name,
            "photo_url": photo_url,
            "category": {
                "name": category_name
            },
            "status": status
            }
    # Добавляем питомца
    status, result = pd.add_new_pets(pets)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400


# 16
def test_get_pet_by_valid_petid(get_some_petid):
    """Позитивный тест. Проверяем получение животного по petid"""

    status, result = pd.get_pet_by_id(get_some_petid['id'])
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == get_some_petid['name']


# 17
@pytest.mark.parametrize('pet_id',
                         [''
                             , generate_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                             , generate_string(10)
                          ],
                         ids=['empty name', 'more than 1000', 'russian', 'RUSSIAN', 'chinese',
                              'specials', 'digits'])
def test_get_pet_be_negative_peid(pet_id):
    """Негативные тесты. Проверяем получение кода ошибки при указании неверного petid животного"""

    status, result = pd.get_pet_by_id(pet_id)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400


# 18
def test_put_pet_by_id_valid_data(get_some_petid, get_some_category_petid):
    """Позитивный тест. Проверяем внесение изменений в данные животного по petid"""
    new_pet = {"name": generate_letters_string(10),
               "photo_url": generate_letters_string(10),
               "category": {
                   "name": get_some_category_petid['name']
               },
               "status": "available"
               }
    status, result = pd.put_pet_by_id(get_some_petid['id'], new_pet)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] != get_some_petid['name']


# 19
@pytest.mark.parametrize('pet_id',
                         [''
                             , generate_letters_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                          ],
                         ids=['empty name', 'more than 1000', 'russian', 'RUSSIAN', 'chinese',
                              'specials'])
@pytest.mark.parametrize('new_pet_name',
                         [''
                             , generate_letters_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                          ],
                         ids=['empty name', 'more than 1000', 'russian', 'RUSSIAN', 'chinese',
                              'specials'])
@pytest.mark.parametrize('new_pet_photo_url',
                         [''
                             , generate_letters_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                          ],
                         ids=['empty name', 'more than 1000', 'russian', 'RUSSIAN', 'chinese',
                              'specials'])
@pytest.mark.parametrize('new_pet_category_name',
                         [''
                             , generate_letters_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                          ],
                         ids=['empty name', 'more than 1000', 'russian', 'RUSSIAN', 'chinese',
                              'specials'])
@pytest.mark.parametrize('new_pet_status',
                         [''
                             , generate_letters_string(1001)
                             , russian_chars()
                             , russian_chars().upper()
                             , chinese_chars()
                             , special_chars()
                          ],
                         ids=['empty name', 'more than 1000', 'russian', 'RUSSIAN', 'chinese',
                              'specials'])
def test_put_pet_by_id_negative_data(pet_id, new_pet_name, new_pet_photo_url, new_pet_category_name, new_pet_status):
    """Негативные тесты. Проверяем получение кода ошибки при внесении изменений в данные животного по некорректному
    petid и с некорректными данными"""
    new_pet = {"name": new_pet_name,
               "photo_url": new_pet_photo_url,
               "category": {
                   "name": new_pet_category_name
               },
               "status": new_pet_status
               }
    status, result = pd.put_pet_by_id(pet_id, new_pet)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400


# 20
def test_successful_del_pet_by_id(get_some_petid):
    """Проверяем возможность удаления питомца"""
    status, result = pd.del_pet_by_id(get_some_petid['id'])
    print(result)
    assert status == 204
