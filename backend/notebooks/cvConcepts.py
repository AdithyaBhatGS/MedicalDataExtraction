import cv2
from PIL import Image 

# converts the gray scale image into values ranging from 0-255

# 0->dark(black) ,255->light(white)  

# flags=cv2.IMREAD_GRAYSCALE->to load the image in grayscale mode

img_of_num=cv2.imread(r'backend\notebooks\dark_image.jpg',flags=cv2.IMREAD_GRAYSCALE)

# print(type(img_of_num))
# print(img_of_num)

# to display the image by taking array of values as parameter
# Image.fromarray(img_of_num).show()

# Check difference between simple thresolding vs adaptive thresolding

# Simple thresold->A technique where for each pixel of the image we check wheather its greater than global thresold ,if yes then set it to 255 else set it to 0

# code for simple thresold

# _ = means ignore the variable

# cv2.thresold(ndarray representing pixels of image,thresold value,max_value,flag)

# _,new_imag=cv2.threshold(img_of_num,150,255,cv2.THRESH_BINARY)

# we use global thresold

# Adaptive thresold->A technique where for each pixel algorithm will assign the different values(not confined to 0 and 255 but any value in between this range) 

# Adaptive thresold is good when we have taken images which contains different lighting conditions in different areas

# 61 -> block size(determines the size of the neighbourhood area)

# 11 -> constant that will be subtracted from the gaussian sum

# ADAPTIVE_THRESH_GAUSSIAN_C -> technique through which we determine the thresold value for each pixel

# here we will enhance the image
new_imag=cv2.adaptiveThreshold(img_of_num,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,61,11)

# print(type(new_imag))

# convert ndarray of enhanced image to image and display it
Image.fromarray(new_imag).show()