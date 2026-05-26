from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "Lab Radar"
    app_env: str = "development"
    log_level: str = "INFO"

    api_host: str = "127.0.0.1"
    api_port: int = 8000
    allowed_origins: list[str] = Field(default_factory=lambda: ["http://localhost:3000"])

    openai_api_key: str | None = None
    openai_chat_model: str = "gpt-4o"
    openai_embedding_model: str = "text-embedding-3-large"

    vector_db_provider: str = "qdrant"
    qdrant_url: str = "http://localhost:6333"
    qdrant_api_key: str | None = None
    qdrant_collection: str = "professor_profiles"
    chroma_persist_directory: str = ".chroma"

    reranker_provider: str = "none"
    cohere_api_key: str | None = None
    cohere_rerank_model: str = "rerank-multilingual-v3.0"

    raw_data_dir: str = "data/raw"
    processed_data_dir: str = "data/processed"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
