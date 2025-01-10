import cv2
import pytesseract

def get_image():
    # direct before we attach front-end
    return "IMG_3141.jpg"

def process_image_with_tesseract(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Unable to read image at {image_path}")
        return

    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(image)
    lines = text.split("\n")
    for line in lines:
        print(line)


def main():
    image_path = get_image()
    process_image_with_tesseract(image_path)

if __name__ == '__main__':
    main()