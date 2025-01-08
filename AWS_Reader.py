import json
import cv2
import pytesseract
from openai import OpenAI


def prepare_image(image):
    return image

def extract_text(image):
    text = ''
    return text

def ai_extract_data(text):
    json_data = json.loads(text)
    return json_data

if __name__ == '__main__':
    image = "IMG_3141"
    preped_image = prepare_image(image)
    text = extract_text(preped_image)
    json_data = ai_extract_data(text)
    print(json_data)
    # call database options to save data from image
    # also store image in database