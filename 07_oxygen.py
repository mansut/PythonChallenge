from PIL import Image
import requests
from io import BytesIO

imageUrl = r"http://www.pythonchallenge.com/pc/def/oxygen.png"
response = requests.get(imageUrl)
img = Image
img = Image.open(BytesIO(response.content))

y = img.size[1] // 2
tileSize = 7
x0 = tileSize//2
stepsNumber = img.width // tileSize

p0 = img.getpixel((x0,y))

values = []
for n in range(0,stepsNumber):
    xCoordinate = x0 + n * tileSize
    pixel = img.getpixel((xCoordinate,y))
    values.append(chr(pixel[0]))

print("".join(values))

#smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]bf
nextLevel = [105, 110, 116, 101, 103, 114, 105, 116, 121]
values.clear()
for n in nextLevel:
    values.append(chr(n))

print("".join(values))

#integrity