import json
import os

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract-OCR\tesseract.exe'
dic={}
f=open('data3.json','w')
for i in range(6524):
    im = Image.open('test/' + str(i) + '.jpg')
    text = pytesseract.image_to_string(im, lang='chi_sim')
    dic[i] = text
    print(i)
j=json.dumps(dic)
f.write(j)
f.close()
