install:
	poetry add ${LIB}

migrate-create:
	alembic revision --autogenerate -m ${MIGRATION}

migrate-apply:
	alembic upgrade head

run:
	poetry run uvicorn app.main:app --host localhost --port 8000 --reload --env-file ${ENV}