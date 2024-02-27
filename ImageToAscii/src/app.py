from PIL import Image, ImageOps, ImageFont, ImageDraw
import math

chars = "$@B%8&WM#*oahkbpqwmZO0QLCJUYXzcunxrjft/\\|()1[]?-_+~<>i!l;:,\"^`'. "[::-1]

charLength = len(chars)
interval = charLength/256

#witdh and height of an individual char
charH = 18
charW = 10
charRatio = charW/charH

#function returning correct character for a pixel
def getChar(pixInt):
    return chars[math.floor(pixInt*interval)]

font_ = ImageFont.truetype('Lucon.ttf', 15)

scale = 0.2
im = Image.open('photo.jpg')
text_file = open("output.txt", "w")

im = im.resize((int(scale*im.width), int(scale*im.height*charRatio)), Image.NEAREST)
width, height = im.size
pix = im.load()

outputImage = Image.new('RGB', (charW*width, charH*height), color = (0, 0, 0))
draw = ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        r ,g ,b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))
        draw.text((j*charW, i*charH), getChar(h), font = font_, fill = (r, g, b))
    text_file.write('\n')
        
outputImage.save('output.jpg')
