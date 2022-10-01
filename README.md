# Техническое задание от компании Каналсервис

Ознакомиться с работой можно [по этой ссылке](https://unwinddigital.notion.site/unwinddigital/Python-1fdcee22ef5345cf82b058c333818c08)

## Как запустить?

Перед сборкой создайте файл <code>.env</code> в папке <b>server</b> со следующими переменными: <br>
<code>DJANGO_SECRET_KEY</code><br>
<code>DJANGO_DEBUG</code><br>
<code>POSTGRES_DB=postgres</code><br>
<code>POSTGRES_USER=postgres</code><br>
<code>POSTGRES_PASSWORD=postgres</code><br>
<code>POSTGRES_HOST=db</code><br>
<code>POSTGRES_PORT=5432</code><br>
<code>TELEGRAM_BOT_TOKEN</code><br>
<code>TELEGRAM_USER_ID</code><br>


# Для сборки
<code>docker-compose up -d --build</code>


docker-compose exec server poetry run python manage.py migrate
docker-compose exec server poetry run python manage.py createsuperuser
docker-compose exec server poetry run python create_scheduler.py

## 
