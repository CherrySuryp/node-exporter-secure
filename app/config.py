import os
from typing import Literal

from pydantic import Field, HttpUrl, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

dir_path = os.path.dirname(os.path.realpath(__file__))
env_path = os.path.join(dir_path, "../.env")
model_config = SettingsConfigDict(env_file=env_path, env_file_encoding="utf-8")


class Config(BaseSettings):
    model_config = model_config

    ENV: Literal["DEV", "PROD"] = Field(default="PROD")
    API_BEARER_TOKEN: SecretStr
    METRICS_ROUTE: str = Field(default="/metrics")
    NODE_EXPORTER_METRICS_PATH: HttpUrl = Field(default="http://node-exporter:9100/metrics")

    @property
    def is_dev_env(self):
        return self.ENV == "DEV"


config = Config()
