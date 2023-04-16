from pydantic import AnyHttpUrl, BaseSettings, HttpUrl, validator
from typing import List, Optional, Union
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DATABASE_URL: str = os.environ.get("DATABASE_URL")

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        os.environ.get("URL_ONE"),
        os.environ.get("URL_TWO"),
    ]

    SMTP_SERVER: str = os.environ.get("SMTP_SERVER")
    SMTP_PORT: str = os.environ.get("SMTP_PORT")
    SMTP_USERNAME: str = os.environ.get("SMTP_USERNAME")
    SMTP_PASSWORD: str = os.environ.get("SMTP_PASSWORD")
    SENDGRID_API_KEY: str = os.environ.get("SENDGRID_API_KEY")

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = "CRUD FASTAPI"
    SENTRY_DSN: Optional[HttpUrl] = None

    class Config:
        case_sensitive = True


settings = Settings()
