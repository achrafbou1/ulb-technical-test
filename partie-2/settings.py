from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_URL: str = "https://b0s0kwos00g48ow8cg0skg4w.89.116.111.143.sslip.io"
    BULLETIN_OUTPUT_PATH: str = "bulletin.csv"
    RAPPORT_ANOMALIES_OUTPUT_PATH: str = "rapport_anomalies.json"

settings = Settings()