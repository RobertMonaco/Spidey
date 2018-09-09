#Spidey.py
#Robert Monaco - Cody Poteet - Daniel Schon - Daniel Chambers - Lilia Williams
#Software Engineer I - Rafal Jabrzemski
######################################################################################
import io
import os
from google.cloud import vision
from google.cloud.vision import types
from google.cloud.vision import ImageAnnotatorClient
import PIL
from PIL import Image
from google.cloud import storage
from django.core.files.storage import default_storage

MY_BUCKET = 'cs4263spidey'

def analyze(file_path):

    # Pass image into Google API
    # Instatiate client
    cl = ImageAnnotatorClient()

    # Load image into memory from cloud storage
    client = storage.Client()
    bucket = client.get_bucket(MY_BUCKET) 
    blob = bucket.get_blob(file_path)
    img_content = blob.download_as_string()

    # Import image
    img = types.Image(content=img_content)

    # Get response from client, assign labels
    resp = cl.label_detection(image=img)
    labels = resp.label_annotations

    # return the list of label descriptions
    return list(map(lambda label: label.description, labels))
