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
    def __init__(self,name = "Unidentified Spider",latin = "Unknown",venomous = "Unknown",bit_text = "If bitten by an unidentified spider you should clean the wound, apply a compress, and consult a medical professional if pain persists.", icon_path = "static/icons/unknown.png"):
        self.com_name = "Unidentified Spider"
        self.sci_name = "Unknown"
        self.type_spider = "Unknown"
        self.help = "If bitten by an unidentified spider you should clean the wound, apply a compress, and consult a medical professional if pain persists."
        self.icon_path = "icons/unknown.png"

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

    # Import image
    img = types.Image(content=img_content)

    # Get response from client, assign labels
    resp = cl.web_detection(image=img)
    annotations = resp.web_detection

    if annotations.web_entities:
        for entity in annotations.web_entities:
            if entity == "Spider" or entity == "Tarantula":
                is_spider = True      
        if not is_spider:
            return Spider("", "","Uhhh...","Spidey could not identify a spider in this picture","icons/notaspider.png")

        #Find out if the spider is in our dictionary   
        for entity in annotations.web_entities:
            key = str(entity.description).lower().replace('spider','').trim()
            if key in spider_dict:
                #Accepted spider
                return Spider(str(entity.description),spider_dict[key]["Scientific Name"],spider_dict[key]["Type"],spider_dict[key]["Help"],"icons/" + spider_dict[key]["Type"].lower() +'.png')
        
        if is_spider:
            return Spider()
    else:
        return Spider("", "","Uhhh...","Spidey could not identify a spider in this picture","icons/notaspider.png")
