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
import logging

MY_BUCKET = 'cs4263spidey'

class Spider:
    def __init__(self,name = "Unidentified Spider",latin = "Unknown",venomous = "Unknown",bit_text = "If bitten by an unidentified spider you should clean the wound, apply a compress, and consult a medical professional if pain persists.", icon_path = "static/icons/unknown.png"):
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
    spider_dict = json.load(open(spider_json_path,'rb'))

    # Pass image into Google API
    # Instatiate client
    cl = ImageAnnotatorClient()

    # Load image into memory from cloud storage
    client = storage.Client()
    bucket = client.get_bucket(MY_BUCKET) 
    blob = bucket.get_blob(file_path)
    img_content = blob.download_as_string()
    
    logs = []
    logs.append("filepath: " + file_path)

    # Import image
    img = types.Image(content=img_content)

    # Get response from client, assign labels
    resp = cl.web_detection(image=img)
    annotations = resp.web_detection

    if annotations.web_entities:
        is_spider = False
        
        logs.append("Keys: ")
        for entity in annotations.web_entities:
            key = str(entity.description).lower()
            logs.append(key)
            if key in spider_dict:
                #Accepted spider
                return Spider(str(entity.description),spider_dict[key]["Scientific Name"],spider_dict[key]["Type"],spider_dict[key]["Help"],"icons/" + spider_dict[key]["Type"].lower() +'.png')
            if key == "spider":
                is_spider = True
        
        logs.append("Is spider: " + str(is_spider))
        if is_spider:
            return Spider()
        else:
            return Spider("", "","Uhhh...","Spidey could not identify a spider in this picture","icons/notaspider.png")
            
