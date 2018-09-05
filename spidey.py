#Spidey.py
#Robert Monaco - Cody Poteet - Daniel Schon - Daniel Chambers - Lilia Williams
#Software Engineer I - Rafal Jabrzemski
######################################################################################
import io
import os
import google-cloud-vision
from google.cloud.vision import types
from google.cloud.vision import ImageAnnotatorClient()
import django
import PIL
from PIL import Image

def main():
    file_path = ''
    
    #Django stuff

    #Django gets filepath

    #Pass image into Google API
    #Instatiate client
    cl = ImageAnnotatorClient()

    #Load image into memory
    with io.open(file_path, 'rb') as img_file:
        img_content = img_file.read()

    #Import image
    img = types.Image(content=img_content)

    #Get response from client, assign labels
    resp = cl.label_detection(image=img)
    labels = resp.label_annotations

    #Print results
    print('Labels:')
    for label in labels:
        print(label.description)

if __name__ == '__main__':
    main()