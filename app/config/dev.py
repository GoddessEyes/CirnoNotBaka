from pydantic import BaseSettings


class Settings(BaseSettings):
    bot_token: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


TORTOISE_ORM = {
    'connections': {'default': 'postgres://postgres:postgres@localhost:5432/cirna'},
    'apps': {
        'cirna': {
            'models': ['app.models', 'aerich.models'],
            'default_connection': 'default',
        },
    },
}

config = Settings()
