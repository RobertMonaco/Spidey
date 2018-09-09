#Spidey.py
#Robert Monaco - Cody Poteet - Daniel Schon - Daniel Chambers - Lilia Williams
#Software Engineer I - Rafal Jabrzemski
######################################################################################
import io
import os
import json
import google-cloud-vision
from google.cloud import vision
from google.cloud.vision import types
from google.cloud.vision import ImageAnnotatorClient
import PIL
from PIL import Image
from google.cloud import storage
from django.core.files.storage import default_storage

MY_BUCKET = 'cs4263spidey'

class Spider:
    def __init__(self):
        self.com_name = ""
        self.sci_name = ""
        self.type = ""
        self.help = ""

    def __init__(self,name,latin,venomous,bit_text):
        self.com_name = name
        self.sci_name = latin
        self.type_spider = venomous
        self.help = bit_text

    def com_name(self):
        return self.com_name

    def sci_name(self):
        return self.sci_name

    def type_spider(self):
        return self.type_spider

    def help(self):
        return self.help



def analyze(file_path):
    spider_json_path = 'spiders.JSON'
    spider_dict = json.loads(open(spider_json_path).read())

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
    resp = cl.web_detection(image=img)
    annotations = resp.web_detection

    if annotations.web_entities:
        is_spider = False
        for entity in annotations.web_entities:
            if str(entity.description) in spider_dict:
                #Accepted spider
                return Spider(str(entity.description),spider_dict[str(entity.description)]["Scientific Name"]
                    ,spider_dict[str(entity.description)]["Type"],spider_dict[str(entity.description)]["Help"])
            if str(entity.description) == "Spider":
                is_spider = True
        if is_spider:
            
    # return results
    return labels

