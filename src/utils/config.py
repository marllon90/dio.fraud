import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    endponit = os.getenv("ENDPOINT")
    subscription_key = os.getenv("SUBSCRIPTION_KEY")
    location = os.getenv("LOCATION")
    azure_connection_string = os.getenv("AZURE_CONNECTION_STRING")
    container_name = os.getenv("CONTAINER_NAME")
