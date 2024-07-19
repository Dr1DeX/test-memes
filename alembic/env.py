import asyncio

from logging.config import fileConfig

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine

from app.infrastructure.database import Base
from app.posts.models import Posts
from app.settings import settings


config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)


target_metadata = Base.metadata


def do_run_migrations(connection):
    context.configure(
        compare_type=True,
        target_metadata=target_metadata,
        dialect_opts={"paramstyle": "named"},
        connection=connection,
        include_schemas=True,
        version_table_schema=target_metadata.schema,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online() -> None:
    """Run migrations in 'online' mode. """

    connectable = create_async_engine(url=settings.db_url, future=True)

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

asyncio.run(run_migrations_online())
