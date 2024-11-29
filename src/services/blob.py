import os

import streamlit
from azure.storage.blob import BlobServiceClient

from utils.config import Config


def upload(file, filename):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(
            Config.azure_connection_string)
        blob_client = blob_service_client.get_blob_client(
            Config.container_name, filename)
        blob_client.upload_blob(file, overwrite=True)
        return blob_client.url
    except Exception as e:
        streamlit.write(f"An error occurred: {e}")
        return False
