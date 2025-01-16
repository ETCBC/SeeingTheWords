import requests
import json
import random
import cameralyze
import os
model_dict = {"human_dec":'4ee0e879-bf7b-4500-bc4d-d1889f6af714', "age_sex" : '2afbc02f-67c9-4eab-a43d-dcf464d50396' }
model = "4ee0e879-bf7b-4500-bc4d-d1889f6af714"
key = "??????"


def call_cameralyze(image):
  connector = cameralyze.Connect(api_key=key)

  payload = {
    "itemUuid": model_dict['age_sex'],
    "image": image,
    "apiKey": key,
    "rawResponse": True,
    "configuration": {
      "confidence": 90,
      "labels": []
  }
  }

  response = requests.post("https://run.plugger.ai/", json=payload)

  return response.json()


