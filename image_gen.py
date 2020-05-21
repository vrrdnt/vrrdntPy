







#thumbnail

# Generate thumbnail.jpg.
shutil.copy('image.jpg', 'thumbnail.jpg')
thumbnail = Image.open("thumbnail.jpg")
size = (1920, 1080)
thumbnail = ImageOps.fit(thumbnail, size, Image.ANTIALIAS)
thumbnail.save(
    'thumbnail.jpg', format='JPEG', optimized=True, subsampling=0, quality=85)