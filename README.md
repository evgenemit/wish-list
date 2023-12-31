# WishList

Это простое веб-приложение, которое позволяет пользователям создавать и управлять своим списком желаний. Разработано на Python 3 и Django 4.

## Особенности

- Регистрация пользователей.
- Добавление и удаление элементов списка желаний.
- Бронирование элементов списка желаний.
- Возможность поделится ссылкой на свой список желаний с друзьями. Ссылку можно найти на странице **Профиль**, при этом для бронирования желаний регистрация необязательна.
- Управление списком желаний через API.

## Установка и запуск

1. Создайте файлы `.env` и `.env.docker` с переменными окружения:

```bash
SECRET_KEY=example
DEBUG=False
REDIS_HOST=redis
REDIS_PORT=6379
```

2. Запустите Docker compose up

```bash
docker-compose up -d
```

Теперь приложение доступно по адресу http://127.0.0.1:8000/ .

## API

В этом разделе описано использование API. Жирным шрифтом выделены обязательные параметры.

Ответы содержат поле `status`, которое может быть `ok` или `error`. `ok` означает, что запрос выполнен без ошибок. При `error` в ответе содержится поле `message`, в котором находится текст ошибки.

Для использования API (кроме бронирования и разбронирования желаний) требуется токен, который можно найти на странице **Профиль**.

## Примечание

Верстка приложения рассчитана на мобильные телефоны.
