# Техническое задание от компании Каналсервис

Ознакомиться с работой можно [по этой ссылке](https://unwinddigital.notion.site/unwinddigital/Python-1fdcee22ef5345cf82b058c333818c08)

## Как запустить?

Перед сборкой создайте файл <code>.env</code> в папке <b>server</b> со следующими переменными: <br>
<code>
DJANGO_SECRET_KEY<br>
DJANGO_DEBUG<br>
POSTGRES_DB=postgres<br>
POSTGRES_USER=postgres<br>
POSTGRES_PASSWORD=postgres<br>
POSTGRES_HOST=db<br>
POSTGRES_PORT=5432<br>
TELEGRAM_BOT_TOKEN<br>
TELEGRAM_USER_ID<br>
</code>


# Для сборки
<code>docker-compose up -d --build</code>


docker-compose exec server poetry run python manage.py migrate
docker-compose exec server poetry run python manage.py createsuperuser
docker-compose exec server poetry run python create_scheduler.py

## 
