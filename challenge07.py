import requests
from PIL import Image
from io import BytesIO
import re

imgae = Image.open(BytesIO(requests.get('http://www.pythonchallenge.com/pc/def/oxygen.png').content))
imgWidth = imgae.width
imgHeight = imgae.height
print " Image have width: %d and height: %d"%(imgWidth,imgHeight)

#Doc tat ca pixel nam giua cua anh
row = [imgae.getpixel((x,imgHeight/2)) for x in range(imgWidth)][::7]#Lay 7 vi ta biet chinh xac co 7 pixel bi thay doi gia tri

#Nhan thay co cac diem anh dang biet co cac pixcel bang nhau. Ta thu chuyen cac gia tri nay sang asscii de doc gia tri dac biet
result =''
ords = [r for r,g,b,a in row if r==g==b]
result = "".join(map(chr, ords))
nums = re.findall("\d+",result)
print "".join(map(chr,map(int,nums)))