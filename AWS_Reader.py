import cv2
from PIL import Image
import pytesseract

def get_image():
    # direct before we attach front-end
    return "IMG_3144.jpg"

def process_image_with_tesseract(image_path):
    image = Image.open(image_path)
    if image is None:
        print(f"Error: Unable to read image at {image_path}")
        return
    
    #grayscale image to help OCR
    image = image.convert('L')

    # set tesseract path 
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(image)
    lines = text.split("\n")
    json_data = extract_ai_data(lines)
    return json_data

def extract_ai_data(lines):
    for line in lines:
        print(line)

def main():
    image_path = get_image()
    json_data = process_image_with_tesseract(image_path)
    #print(json_data)

if __name__ == '__main__':
    main()