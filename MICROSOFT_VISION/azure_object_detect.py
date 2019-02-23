import requests
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import patches
from io import BytesIO
import os
import ObjectAPIConfig as cnfg

image_path = os.path.join('images.jpg')
image_data = open(image_path, "rb").read()

subscription_key, object_api_url = cnfg.config();

headers = {'Content-Type': 'application/octet-stream',
           'Ocp-Apim-Subscription-Key': subscription_key}

params = {'visualFeatures': 'Description'}

response = requests.post(object_api_url, params=params, headers=headers, data=image_data)
response.raise_for_status()
objects = response.json()
print(objects)

