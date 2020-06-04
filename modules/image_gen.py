# import shutil
# from PIL import Image, ImageOps
# import json
#
# with open('../settings.json') as config:
#     settings = json.load(config)
#
# # TODO: This could go inside resources.py
#
# # Image formatting
# # Asks the user to supply an image URL or select an image file,
# # and uploads either to Imgur pre-jpg-conversion.
# img_source = easygui.buttonbox(
#     "Enter a URL or choose an image file", choices=["File", "URL"])
# if img_source == "File":
#     img_file = easygui.fileopenbox(
#         msg=None, title=None, filetypes=[["*.jpg", "*.png"]], multiple=False)
#     img = Image.open(img_file)
#     img_to_jpg = img.convert('RGB')
#     img_to_jpg = img.save('image.jpg')
#     upload_img = requests.post(
#         api_url,
#         headers=headers,
#         data={
#             'image': b64encode(open('image.jpg', 'rb').read()),
#             'type': 'base64'
#         })
#     data = json.loads(upload_img.text)['data']
#     print(data)
#     imgur_link = data['link']
#     img = Image.open('image.jpg')
#     resized_image = img.convert('RGB')
#     size = (2560, 1440)
#     resized_image = ImageOps.fit(resized_image, size, Image.ANTIALIAS)
#     resized_image.save('image.jpg', format='JPEG', subsampling=0, quality=100)
# elif img_source == "URL":
#     imageURL = easygui.enterbox("Please enter a direct link to an image.")
#     response = requests.get(imageURL)
#     img = Image.open(BytesIO(response.content))
#     img_to_jpg = img.convert('RGB')
#     img_to_jpg = img.save('image.jpg')
#     upload_img = requests.post(
#         api_url,
#         headers,
#         data={
#             'image': b64encode(open('image.jpg', 'rb').read()),
#             'type': 'base64'
#         })
#     data = json.loads(upload_img.text)['data']
#     imgur_link = data['link']
#     img = Image.open('image.jpg')
#     size = (2560, 1440)
#     resized_image = ImageOps.fit(img_to_jpg, size, Image.ANTIALIAS)
#     resized_image.save('image.jpg', format='JPEG', subsampling=0, quality=100)
#
#
#
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
# size = (1920, 1080)
# thumbnail = ImageOps.fit(thumbnail, size, Image.ANTIALIAS)
# thumbnail.save(
#     'thumbnail.jpg', format='JPEG', optimized=True, subsampling=0, quality=85)
