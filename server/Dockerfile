FROM python:3.10 as builder
COPY . /server
WORKDIR /server
ENV POETRY_VIRTUALENVS_CREATE false
RUN pip install --upgrade pip && pip3 install poetry && poetry install --no-root
