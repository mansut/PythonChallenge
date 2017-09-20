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

values = []
for n in range(0,stepsNumber):
    xCoordinate = x0 + n * tileSize
    pixel = img.getpixel((xCoordinate,y))
    values.append(pixel[0])

print("".join(map(chr,values)))

#smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]bf
nextLevel = [105, 110, 116, 101, 103, 114, 105, 116, 121]
values.clear()
for n in nextLevel:
    values.append(chr(n))

print("".join(values))

#integrity

#www.pythonchallenge.com/pcc/def/integrity.html
#www.pythonchallenge.com/pc/def/integrity.html