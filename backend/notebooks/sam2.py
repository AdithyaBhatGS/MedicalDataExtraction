from pdf2image import convert_from_path

import numpy as np

import cv2

from PIL import Image

# convert_from_path()->takes the pdf document and returns a list of images

# pdf is being converted to images

list_of_images = convert_from_path(r'C:\Users\ADITHYA GS\OneDrive\Documents\Programs\medicalProject\backend\resources\patient_details\pd_1.pdf', poppler_path=r'C:\poppler-23.01.0\Library\bin')

# print(type(list_of_images))

# print(len(list_of_images))

# print(list_of_images)

# displays the converted image
# list_of_images[0].show()
# list_of_images[1].show()

import pytesseract

pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(img):

    # Converting the rgb image to a numpy array and then converting it into grayscale

    gray=cv2.cvtColor(np.array(img),cv2.COLOR_BGR2GRAY)

    # Resizing the image

    # resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])

    # src: It is the required input image, it could be a string with the path of the input image (eg: ‘test_image.png’).
    # dsize: It is the desired size of the output image, it can be a new height and width.
    # fx: Scale factor along the horizontal axis.
    # fy: Scale factor along the vertical axis.
    # interpolation: It gives us the option of different methods of resizing the image.

    resized=cv2.resize(gray,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LINEAR)

    # now apply adaptive thresolding to this resized image

    # Adaptive thresold->A technique where for each pixel algorithm will assign the different values(not confined to 0 and 255 but any value in between this range)

    # Adaptive thresold is good when we have taken images which contains different lighting conditions in different areas

    # 61 -> block size(determines the size of the neighbourhood area)

    # 11 -> constant that will be subtracted from the gaussian sum

    # ADAPTIVE_THRESH_GAUSSIAN_C -> technique through which we determine the thresold value for each pixel

    # here we will enhance the image

    processed_image=cv2.adaptiveThreshold(resized,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,61,11)

    return processed_image

img=preprocess_image(list_of_images[0])
# Image.fromarray(img).show()

# deriving text from the respective image after post processing
text=pytesseract.image_to_string(img,lang='eng')

print(text)
