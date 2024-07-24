install:
	poetry add ${LIB}

migrate-create:
	alembic revision --autogenerate -m ${MIGRATION}

migrate-apply:
	alembic upgrade head

run-post:
	poetry run uvicorn app.posts.main:app --host localhost --port 8001 --reload --env-file ${ENV}

run-s3:
	poetry run uvicorn app.s3.main:app --host localhost --port 8002 --reload --env-file ${ENV}

build:
	docker-compose down
	docker-compose up -d --build
