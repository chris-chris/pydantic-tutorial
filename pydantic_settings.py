import os

from pydantic import BaseSettings


class Settings(BaseSettings):

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


if __name__ == "__main__":
    print(os.environ["REDIS_ADDRESS"])
