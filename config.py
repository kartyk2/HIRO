from typing import Final
from dotenv import load_dotenv, dotenv_values

creds= dotenv_values(".env")

TOKEN :Final = creds.get("TOKEN")
USERNAME : Final = creds.get("USERNAME")

