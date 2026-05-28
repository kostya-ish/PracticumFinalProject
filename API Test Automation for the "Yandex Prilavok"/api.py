import requests

from configuration import URL_SERVICE, CREATE_NEW_ORDER, GET_ORDER_BY_TRACK_ID
from data import ORDER_BODY


def post_new_order():
    """ Создание нового заказа """
    url = URL_SERVICE + CREATE_NEW_ORDER
    payload = ORDER_BODY
    response = requests.post(url, json=payload)
    return response


def get_order_by_track_id(track_id):
    """ Получение заказа по трек номеру """
    url = URL_SERVICE + GET_ORDER_BY_TRACK_ID
    params = {
        "t": track_id
    }
    response = requests.get(url, params=params)
    return response
