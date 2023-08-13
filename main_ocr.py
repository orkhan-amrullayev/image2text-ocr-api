from gradio_client import Client
import re

client_str = "https://jackwrion-ocr.hf.space/"
client = Client(client_str)

path_to_jpeg = "Image 2023-08-13 at 17.42.22.jpeg"


def image2text_ocr(client, path_to_jpeg):  
  response = client.predict(
      path_to_jpeg,	# str (filepath or URL to image) in 'parameter_3' Image component
      fn_index=0)
  
  # Remove HTML tags using regular expressions
  clean_text = re.sub(r'<.*?>', '', response[0])

  # TO-DO
  # clean text by its alignment to left and right

  return clean_text


## inference
output = image2text_ocr(client, path_to_jpeg)
print(output)
