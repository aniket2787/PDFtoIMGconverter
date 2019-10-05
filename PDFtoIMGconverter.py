'''
Author = Aniket
'''
import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from PIL import Image
from PIL import ImageEnhance
import datetime
Tk().withdraw()
filename = askopenfilename()
filepath = filename.split("/")[-1]
if filepath in filename:
    Path = filename.replace(filepath, "")
filepath1 = filepath.split(".")
newPath = Path+filepath1[0]+"/"
if os.path.exists(newPath):
    shutil.rmtree(newPath)
    os.mkdir(newPath)

from pdf2image import convert_from_path
pages = convert_from_path(filename, 500)
cnt = 1
for page in pages:
    page.save(newPath+'out'+str(cnt)+'.jpg', 'JPEG')
    def adjust_sharpness(input_image, output_image, factor):
        image = Image.open(input_image)
        enhancer_object = ImageEnhance.Sharpness(image)
        out = enhancer_object.enhance(factor)
        out.save(output_image)
    def adjust_brightness(input_image, output_image, factor):
        image = Image.open(output_image)
        enhancer_object = ImageEnhance.Brightness(image)
        out = enhancer_object.enhance(factor)
        out.save(output_image)
    def adjust_contrast(input_image, output_image, factor):
        image = Image.open(output_image)
        enhancer_object = ImageEnhance.Contrast(image)
        out = enhancer_object.enhance(factor)
        out.save(output_image)

    if __name__ == '__main__':
        adjust_sharpness(newPath+'out'+str(cnt)+'.jpg', newPath+'out'+str(cnt)+'.jpg', 1.8)
        adjust_brightness(newPath+'out'+str(cnt)+'.jpg', newPath+'out'+str(cnt)+'.jpg', 1.0)
        adjust_contrast(newPath+'out'+str(cnt)+'.jpg', newPath+'out'+str(cnt)+'.jpg', 1.8)
        cnt = cnt + 1
