from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv('.env')


class Postgres(BaseSettings):
    USER: str = "user"
    PASSWORD: str = "123"
    DB: str = "db"
    HOST: str = "localhost"
    PORT: str = "5432"

    class Config:
        env_prefix = 'POSTGRES_'

    def build_url(self) -> str:
        return f'postgresql+asyncpg://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DB}'


class Settings(BaseSettings):
    DEBUG: bool = False
    POSTGRES: Postgres = Postgres()


settings = Settings()
