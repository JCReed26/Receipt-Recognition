import cv2
from PIL import Image
import pytesseract
import openai

# Set your OpenAI API key
openai.api_key = "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"

def get_image():
    # Direct before we attach front-end
    return "IMG_3144.jpg"

def process_image_with_tesseract(image_path):
    image = Image.open(image_path)
    if image is None:
        print(f"Error: Unable to read image at {image_path}")
        return
    
    # Grayscale image to help OCR
    image = image.convert('L')

    # Set tesseract path 
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Perform OCR using pytesseract
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