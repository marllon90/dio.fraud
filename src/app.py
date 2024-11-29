import streamlit
from src.services.blob import upload
from src.services.credicard import get_creditcard_info


def configure_interface():
    streamlit.title("Uploading Files DIO")
    uploaded_file = streamlit.file_uploader(
        "Choose a file", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        file_name = uploaded_file.name

        blob_url = upload(uploaded_file, file_name)

        if blob_url:
            streamlit.write("File uploaded successfully!")
            credit_card_info = get_creditcard_info(blob_url)
            show_image_validation(blob_url, credit_card_info)
        else:
            streamlit.write("Something went wrong. Please try again.")


def show_image_validation(blob_url, credit_card_info):
    streamlit.image(blob_url, use_container_width=True,
                    caption="Uploaded Image")
    streamlit.write("Credit Card Information:")

    if credit_card_info and credit_card_info.get("card_name"):
        streamlit.markdown(
            f"**Bank Name:** {credit_card_info.get('bank_name')}")
        streamlit.markdown(
            f"**Card Number:** {credit_card_info.get('card_number')}")
        streamlit.markdown(
            f"**Card Name:** {credit_card_info.get('card_name')}")
        streamlit.markdown(
            f"**Expiration Date:** {credit_card_info.get('expiration_date')}")
    else:
        streamlit.write("No credit card information found.")


if __name__ == "__main__":
    configure_interface()
