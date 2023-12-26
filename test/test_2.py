import pytest
import logging
from check_post import get_post, create_post
logging.basicConfig(filename="logs.log", encoding="utf8", level=logging.INFO)
logger = logging.getLogger("log")

id_check = 93703
title_check = 'Кунгуская леДяная пешера'

logger.info("Начало выполнения тестов")

def test_1(token):
    output = get_post(token)['data']
    print(output)
    res = []
    for item in output:
        res.append(item['id'])
    if not(id_check in res):
        logging.info("Тест 1")
        logger.warning("Искомый пост по id не найден")
    assert id_check in res


def test_2(token):
    if not ((title_check.lower() in create_post(token)['title'].lower())):
        logging.info("Тест 2")
        logger.warning("Пост был создан под другим именем")
    assert title_check.lower() in create_post(token)['title'].lower()
