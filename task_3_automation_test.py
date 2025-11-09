from api import post_new_order, get_order_by_track_id

# Константин Ищенко, 37-я когорта — Финальный проект. Инженер по тестированию плюс

def test_new_order():
    # Выполнить запрос на создание заказа.
    order = post_new_order()

    # Сохранить номер трека заказа.
    order_json = order.json()
    track_id = order_json["track"]

    # Выполнить запрос на получение заказа по треку заказа.
    track_order = get_order_by_track_id(track_id)

    # Проверить, что код ответа равен 200.
    assert track_order.status_code == 200
