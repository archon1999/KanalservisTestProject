# Техническое задание от компании Каналсервис

Ознакомиться с работой можно [по этой ссылке](https://unwinddigital.notion.site/unwinddigital/Python-1fdcee22ef5345cf82b058c333818c08)

## Как запустить?

Перед сборкой создайте файл <code>.env</code> в папке <b>server</b> со следующими переменными: <br>

Django
* <code>DJANGO_SECRET_KEY</code><br>
* <code>DJANGO_DEBUG</code><br>

Данные для БД
* <code>POSTGRES_DB=postgres</code><br>
* <code>POSTGRES_USER=postgres</code><br>
* <code>POSTGRES_PASSWORD=postgres</code><br>
* <code>POSTGRES_HOST=db</code><br>
* <code>POSTGRES_PORT=5432</code><br>

Токен телеграм бота
* <code>TELEGRAM_BOT_TOKEN</code><br>

Кому отправлять уведомление
* <code>TELEGRAM_USER_ID</code><br>


### Сборка и запуск
<code>docker-compose up -d --build</code><br>

После сборки сделать миграцию данных:
<code>docker-compose exec server poetry run python manage.py migrate</code>

Для создания суперпользователя для входа в страницу администрации:
<code>docker-compose exec server poetry run python manage.py createsuperuser</code>

Создайте объекты для планировщика задач:
<code>docker-compose exec server poetry run python create_scheduler.py</code><br>

Есть два запланированных задач:
  1. <b>update-data</b> - Обновление данных в каждую минуту.
  2. <b>update-ruble-exchange-rate</b> - Обновление курса валюты, рубля к доллару, один раз в день.

  
После сборки и запуска запустятся три сервера на портах <code>8888</code>, <code>8880</code> и <code>4200</code>:
  1. <b>gunicorn</b> - WSGI-сервер.
  2. <b>daphne</b> - ASGI-сервер. Для использования вебсокета.
  3. <b>nginx</b> - SPA-приложение, написанное на <b>Angular</b>.
