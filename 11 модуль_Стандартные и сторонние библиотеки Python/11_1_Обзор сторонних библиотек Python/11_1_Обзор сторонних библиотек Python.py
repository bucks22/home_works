from PIL import Image, ImageDraw, ImageFont
import requests
import sys

# image = Image.open('1.webp')
# image = Image.open('2.png')
image = Image.open('3.jpg')
print(image.size)

"""Получение метаданных exif"""
# exif = image._getexif()
# print(exif)

"""Обрезка изображения"""
# cropped = image.crop((150, 200, 300, 350))
# cropped.save('./cropped1.jpeg')

"""Написание текста на изображении"""
# idraw = ImageDraw.Draw(image)
# text = 'mmiklm'
# font = ImageFont.truetype(font='arial.ttf',size=12)
# idraw.text((10, 50), text, font=font)
# image.save('image_text.jpg')

"""Скачивание изображения по ссылке и сохранение в формате jpg"""
url = 'https://avatars.mds.yandex.net/i?id=380189c0046b942528d6fc8a5ea1a749_l-13452872-images-thumbs&n=13'
try:
    resp = requests.get(url, stream=True).raw
except requests.exceptions.RequestException as e:
    sys.exit(1)

try:
    img = Image.open(resp)
except IOError:
    print("Unable to open image")
    sys.exit(1)

img.save('sid1.jpg', 'jpeg')

"""С помощью библиотек request и PIL я оптимизировал свою рутинную задачу по скачиваю изображений и сохранении в формате 
jpg"""