# Receipt-Recognition

Receipt Reader 
    This file uses the opencv CV2 library and PIL Image library 
    to open the image grayscale the image for better readability 
    It then incorporates Tesseract-OCR with pytesseract to read 
    the text from the image of the receipt. 
    The program then takes the reading and feeds it into chat gpt 
    4o model to return a JSON of the name of the store, its category
    for sorting and a list of items with their costs 

The goal for this is to be used within my databases course project which I just started the course and want 
to utilize this further than just a project for my life automation goals
