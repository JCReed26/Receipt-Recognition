import cv2
from PIL import Image
import pytesseract
import openai
import os 
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def get_image():
    return "IMG_3144.jpg"

def process_image_with_tesseract(image_path):
    image = Image.open(image_path)
    if image is None:
        print(f"Error: Unable to read image at {image_path}")
        return
    image = image.convert('L')

    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    text = pytesseract.image_to_string(image)
    lines = text.split("\n")
    json_data = extract_ai_data(lines)
    return json_data

def extract_ai_data(lines):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant who takes in lines of data to represent to return javascript object notation (JSON) data."
            },
            {
                "role": "user",
                "content": "Given the text extracted from a receipt, which may include additional words at the top and bottom, " +
                           "identify the main category of the purchase for budgeting purposes. Structure your response in JSON format, " +
                           "including the following fields: 'name' for the name of the company, 'category' for the main purchase category, 'items' as an array of objects " +
                           "where each object contains 'item' (the name of the item) and 'cost' (the price of the item), and 'total_amount' " +
                           "for the total cost of all items. Ensure that the JSON output is correctly formatted and includes all necessary " +
                           "information derived from the receipt text. Here is the receipt text to process:\n" + "\n".join(lines)
            }
        ]
    )
    
    json_data = response['choices'][0]['message']['content']
    return json_data

def main():
    image_path = get_image()
    json_data = process_image_with_tesseract(image_path)
    # Print the JSON data
    print(json_data)

if __name__ == '__main__':
    main()