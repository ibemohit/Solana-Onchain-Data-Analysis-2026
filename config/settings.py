import os
from dotenv import load_dotenv

class Settings:

    def __init__(self, env_file: str = ".env"):
        load_dotenv(env_file)

        self.mongo_user = os.getenv("MONGO_USER")
        self.mongo_pass = os.getenv("MONGO_PASS")
        self.mongo_host = os.getenv("MONGO_HOST")
        self.mongo_db = os.getenv("MONGO_DB")

        '''self.solana_rpc = os.getenv(
            "SOLANA_RPC",
            "https://api.mainnet-beta.solana.com"
        )'''

        self._validate()

    def _validate(self):
        missing = []
        if not self.mongo_user:
            missing.append("MONGO_USER")
        if not self.mongo_pass:
            missing.append("MONGO_PASS")
        if not self.mongo_host:
            missing.append("MONGO_HOST")

        if missing:
            raise EnvironmentError(
                f"Missing required environment variables: {', '.join(missing)}"
            )

    @property
    def mongo_uri(self) -> str:
        #Connection URI
        return (
            f"mongodb+srv://{self.mongo_user}:"
            f"{self.mongo_pass}@{self.mongo_host}/"
            f"{self.mongo_db}?retryWrites=true&w=majority"
        )
settings = Settings()