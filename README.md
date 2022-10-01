# Техническое задание от компании Каналсервис

Ознакомиться с работой можно [по этой ссылке](https://unwinddigital.notion.site/unwinddigital/Python-1fdcee22ef5345cf82b058c333818c08)

## Как запустить?

Перед сборкой создайте файл <code>.env</code> в папке <b>server</b> со следующими переменными:
<code>
DJANGO_SECRET_KEY
DJANGO_DEBUG

POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432

TELEGRAM_BOT_TOKEN=
TELEGRAM_USER_ID=
</code>


# Для сборки
<code>docker-compose up -d --build</code>


docker-compose exec server poetry run python manage.py migrate
docker-compose exec server poetry run python manage.py createsuperuser
docker-compose exec server poetry run python create_scheduler.py

## 
