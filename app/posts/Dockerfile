FROM python:3.12

WORKDIR /public_api

COPY /pyproject.toml .

RUN pip install poetry
RUN poetry install

COPY .. .

CMD ["poetry", "run", "uvicorn", "app.posts.main:app", "--host", "0.0.0.0", "--port", "8001"]