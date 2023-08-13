# Image to Text OCR Script

This script performs Optical Character Recognition (OCR) on an image and extracts clean text. It utilizes the `gradio_client` library to interact with an OCR service.

## Prerequisites

- Python 3.x
- Install the `gradio_client` library:

  ```bash
  pip install gradio_client
  ```

# Usage
Run the script from the command line with the following options:

  ```bash
python main_ocr.py --client_url "https://orkhan-image2text-ocr.hf.space/" --image_path "path/to/your/image.jpg"
```
* `--client_url`: URL for the gradio_client (default: "https://orkhan-image2text-ocr.hf.space/")
* `--image_path`: Path to the image file for OCR processing
You can omit the --client_url and --image_path options to use the default values defined in the script.

# Example Usage
```bash
python main_ocr.py --image_path "My Image 2023.jpeg"
```
or:
```bash
python main_ocr.py --client_url "https://orkhan-image2text-ocr.hf.space/" --image_path "C:\Users\your_username\Downloads\some_pic_with_text.jpeg"
```

# Script Description
The script contains the following components:

- `clean_text_from_html_tags`: A function to remove HTML tags from text using regular expressions.
- `image_to_text_ocr`: A function to perform OCR on an image and extract clean text.
- `main`: The main function that parses command-line arguments, initializes the gradio_client, and calls the OCR functions.
The script accepts the `--client_url` and `--image_path` command-line arguments. The `--client_url` argument specifies the URL for the gradio_client, and the `--image_path` argument specifies the path to the image file for OCR.

Feel free to customize this README further to match your script's details and requirements.

# Future Improvements
- cleaning steps should be improved in this function: `clean_text_from_html_tags`
