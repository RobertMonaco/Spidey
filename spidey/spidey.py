#Spidey.py
#Robert Monaco - Cody Poteet - Daniel Schon - Daniel Chambers - Lilia Williams
#Software Engineer I - Rafal Jabrzemski
######################################################################################
import io
import os
import json
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
        self.com_name = "Unidentified Spider"
        self.sci_name = "Unknown"
        self.type = "Unknown"
        self.help = "If bitten by an unidentified spider you should clean the wound, apply a compress, and consult a medical professional if pain persists."
        self.icon_path = "static/icons/unknown.png"

    def __init__(self,name,latin,venomous,bit_text, icon_path):
        self.com_name = name
        self.sci_name = latin
        self.type_spider = venomous
        self.help = bit_text
        self.icon_path = icon_path

    def com_name(self):
        return self.com_name

    def sci_name(self):
        return self.sci_name

    def type_spider(self):
        return self.type_spider

    def help(self):
        return self.help

    def icon_path(self):
        return self.icon_path



def analyze(file_path):
    spider_json_path = 'spidey/spiders.JSON'
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
                    ,spider_dict[str(entity.description)]["Type"],spider_dict[str(entity.description)]["Help"],"static/icons/" + spider_dict[str(entity.description)]["Type"].lower() +'.png')
            if str(entity.description) == "Spider":
                is_spider = True
        
        if is_spider:
            return Spider()
        else:
            return Spider("", "","Uhhh...","Spidey could not identify a spider in this picture","status/icons/notaspider.png")


