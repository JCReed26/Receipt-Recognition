
import boto3

#this is from a 1135page developer guide for Rekognition
#page 666 is the python code below
def detect_text(bucket, photo):

    session = boto3.Session(profile_name='default')
    client = session.client('rekognition')

    response = client.detect_text(Image={'S3Object': {'Bucket': bucket, 'Name': photo}})

    textDetections = response['TextDetections']
    print('Detected text:' + text['DetectedText'])
    print(f"Confidence: {text['Confidence']}")
    print(f"Id: {text['Id']}")
    if 'ParentId' in text:
        print(f"Parent Id: {text['ParentId']}")
    print(f"Type: {text['Type']}")
    print()

    return len(textDetections)

#this is the github version
if __name__ == "__main__":

    bucket = 'bucketname'
    photo = 'photo.jpg'

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