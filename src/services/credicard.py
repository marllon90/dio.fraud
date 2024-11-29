from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from azure.core.credentials import AzureKeyCredential

from utils.config import Config


def get_creditcard_info(card_url):
    try:
        credential = AzureKeyCredential(Config.subscription_key)
        document_client = DocumentIntelligenceClient(
            endpoint=Config.endponit, credential=credential)

        card_info = document_client.begin_analyze_document(
            "prebuilt-creditCard", AnalyzeDocumentRequest(url_source=card_url))

        result = card_info.result()

        for document in result.documents:
            fields = document.get("fields", {})

            return {
                "card_name": fields.get("CardHolderName", {}).get("content"),
                "card_number": fields.get("CardNumber", {}).get("content"),
                "expiration_date": fields.get("ExpirationDate", {}).get("content"),
                "bank_name": fields.get("BankName", {}).get("content")
            }

    except Exception as e:
        return f"An error occurred: {e}"
