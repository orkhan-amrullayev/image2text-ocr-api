import argparse
from gradio_client import Client
import re

# Constants
DEFAULT_CLIENT_URL = "https://orkhan-image2text-ocr.hf.space/"
# DEFAULT_IMAGE_PATH = "assets/my_picture.jpeg"
RESPONSE_TEXT_INDEX = 0


def clean_text_from_html_tags(text):
    """Remove HTML tags using regular expressions."""
    clean_text = re.sub(r'<.*?>', '', text)

    # TO-DO: Additional cleaning based on text alignment
    # 
    #
    
    return clean_text


def image_to_text_ocr(client, image_path):
    """Perform OCR on the image and extract clean text."""
    try:
        response = client.predict(image_path, fn_index=0)
        response = clean_text_from_html_tags(response[RESPONSE_TEXT_INDEX])


        return response
    except Exception as e:
        print("Error during OCR:", str(e))
        return None


def main(args):
    client = Client(args.client_url)

    cleaned_output = image_to_text_ocr(client, args.image_path)
    if cleaned_output:
        print("Cleaned Output:", cleaned_output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform OCR on an image and extract clean text.")
    parser.add_argument("--client_url", type=str, default=DEFAULT_CLIENT_URL,
                        help="URL for the gradio_client (default: {})".format(DEFAULT_CLIENT_URL))
    parser.add_argument("--image_path", type=str,
                        help="Path to the image file")

    args = parser.parse_args()
    main(args)

    # python main_ocr.py --image_path "My Image 2023.jpeg"
    # python main_ocr.py --client_url "https://orkhan-image2text-ocr.hf.space/" --image_path "C:\Users\o.amrullayev\Downloads\some pic with text.jpeg"
