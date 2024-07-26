FROM python:3.12

WORKDIR /public_api

COPY /pyproject.toml .

RUN pip install poetry
RUN poetry install

COPY .. .
