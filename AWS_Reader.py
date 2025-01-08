import boto3

#this is the github version
if __name__ == "__main__":

    bucket = 'jims-receipt-bucket'
    photo = 'IMG_3138.jpg'

    client = boto3.client('rekognition')

    response = client.detect_text(Image={'S3Object': {'Bucket': bucket, 'Name': photo}})

    textDirections = response['TextDetections']
    print(response)

    for text in textDirections:
        print(f"Detected Text: {text['DetectedText']}")
        print(f"Confidence: {text['Confidence']}")
        print(f"Id: {text['Id']}")
        if 'ParentId' in text:
            print(f"Parent Id: {text['ParentId']}")
        print(f"Type: {text['Type']}")
        print()