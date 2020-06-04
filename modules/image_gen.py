import shutil
from PIL import Image, ImageOps
import json
import requests
from base64 import b64encode

with open('../settings.json') as config:
    settings = json.load(config)

# Network open: Image.open(BytesIO(response.content))
# Get link of imgur upload: data = json.loads(upload_img.text)['data']
#                                  imgur_link = data['link']


def fit_image(image):
    img = Image.open(image)
    image_dimensions = (settings['video_width'], settings['video_height'])
    resized_image = ImageOps.fit(img, image_dimensions, Image.ANTIALIAS)
    resized_image.save('../working/modified_image.jpg', format='JPEG', subsampling=0, quality=100)


# # Upload image
# # Imgur authentication section
# client_id = settings['imgur_client_id']
#
# imgur_upload_endpoint = "https://api.imgur.com/3/upload"
#
# headers = {"Authorization": "Client-ID " + client_id}
#
#
# def imgur_upload(image): # TODO: This is the file upload one. Need to mix URL/disk image upload.
#     image_upload = requests.post(
#         imgur_upload_endpoint,
#         headers=headers,
#         data={
#             'image': b64encode(open('image.jpg', 'rb').read()),
#             'type': 'base64'
#         })
#     data = json.loads(imgur_upload.text)['data']
#     imgur_link = data['link']
#
#
#
# # thumbnail
#
# # Generate thumbnail.jpg.
#
#
# shutil.copy('image.jpg', 'thumbnail.jpg')
# thumbnail = Image.open("thumbnail.jpg")
# size = (settings['thumbnail_width'], settings['thumbnail_height'])
# thumbnail = ImageOps.fit(thumbnail, size, Image.ANTIALIAS)
# thumbnail.save(
#     'thumbnail.jpg', format='JPEG', optimized=True, subsampling=0, quality=85)
