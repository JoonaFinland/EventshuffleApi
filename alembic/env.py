from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context
from app import models
from app.core.config import AppSettings
config = context.config

settings = AppSettings()

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

DATABASE_URL = str(settings.DATABASE_URL)
db_driver = settings.DATABASE_URL.scheme
db_driver_parts = db_driver.split("+")
if len(db_driver_parts) > 1:  # e.g. postgresql+asyncpg
    sync_scheme = db_driver_parts[0].strip()
    DATABASE_URL = DATABASE_URL.replace(  # replace with sync driver
        db_driver, sync_scheme
    )

config.set_main_option("sqlalchemy.url", DATABASE_URL)

target_metadata = models.Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
