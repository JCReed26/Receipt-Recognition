from PIL import Image
import pytesseract
from openai import OpenAI
import os 
from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import io

#get env and api key
load_dotenv()
client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")


#create running app 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root(): 
    return {"message": "API is running"}

@app.get("/health")
async def health():
    return {"message": "API is up"}

#this should be looked into to optimize the image processing (maybe add in a ml framework)
#async allow func to wait for image
async def process_image_with_tesseract(image_data):
    print("inside tesseract pre try")
    try:
        print("inside try")
        # converts to bytes then to image 
        image = Image.open(io.BytesIO(image_data))
        image = image.convert("L") # makes it easier to differentiate between black and white


        #local tesseract-ocr WILL NOT WORK WITHOUT
        # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        #docker tesseract-ocr WILL NOT WORK WITHOUT
        pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract' #the linux path in docker

        #process image to output
        text = pytesseract.image_to_string(image)
        lines = text.split("\n")
        json_data = extract_ai_data(lines)
        return json_data
    except IOError as e:
        print(f"IO error: {str(e)}")
        raise HTTPException(status_code=400, detail="invalid image data")
    except Exception as e:
        print(f"unexpexted error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


#this will need to be optimized to offer more accurate results 
def extract_ai_data(lines):
    response = client.chat.completions.create(
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
    
    json_data = response.choices[0].message.content
    return json_data

@app.post("/process-image") #POST request ... is the right way? but why?
async def process_image(file: UploadFile = File(...)): 
    try:
        if not file.content_type.startswith("image/"):
            raise HTTPException(status_code=400, detail="Must upload a photo")

        print("inside process image")
        print(f"Received file {file.filename}, content type {file.content_type}")
        contents = await file.read()
        print(f"Received file contents {contents}")
        return await process_image_with_tesseract(contents)
    except Exception as e: 
        print(f"Error processing image: {e}")
        raise HTTPException(status_code=500, detail=str(e))