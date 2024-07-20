FROM python:3.12

WORKDIR /app

COPY /pyproject.toml .

RUN pip install poetry
RUN poetry install

COPY .. .

CMD ["poetry", "run", "uvicorn", "app.s3.main:app", "--host", "0.0.0.0", "--port", "8002"]