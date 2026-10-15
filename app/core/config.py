from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    SERVICE_NAME: str = "Inventory"
    ENV: str = "local"
    AUTH_TYPE: str = "jwt_rbac"  # none | api_key | jwt_rbac
    CACHE_ENABLED: bool = True
    QUEUE_ENABLED: bool = True
    DATABASE: str = "postgresql"  # none | postgresql | mongodb
    JWT_SECRET: str = "32818c1d3779c555651af33ce2a0c155e477ed1445aeb785a64eb8ef840e9bcd"
    JWT_ALGORITHM: str = "HS256"
    # مقدار پیش‌فرض برای توسعهٔ لوکال؛ در .env (که در .gitignore است) override کنید.
    DATABASE_URL: str = "postgresql+asyncpg://forge:change-me@localhost:5432/inventory_backend"


settings = Settings()
