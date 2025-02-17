# Receipt-Recognition

Receipt Reader 
    This file uses PIL Image library 
    to open the image grayscale the image for better readability 
    It then incorporates Tesseract-OCR with pytesseract to read 
    the text from the image of the receipt. 
    The program then takes the reading and feeds it into chat gpt 
    4o model to return a JSON of the name of the store, its category
    for sorting and a list of items with their costs 

This is to be developed into an application purely for personal use to help me take better control of my finances.
This will make it easier since I just have to take a picture and it completes the rest for me.
