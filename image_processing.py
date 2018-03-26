import cv2
import numpy as np 
import math
def fill(image, dark):
	'''
	image: A cv2/np array containing an image that is smaller than 128x128
	dark(bool): If the original image had a dark or light background
	'''
	height, width, channels = image.shape
	color = 0
	if not dark:
		color = 255
	y_pad = (int(math.floor((128-height)/2)),int(math.ceil((128-height)/2)))
	x_pad = (int(math.floor((128-width)/2)),int(math.ceil((128-width)/2)))
	image = np.pad(image, [y_pad, x_pad,(0,0)], mode = 'constant', constant_values = color)
	return image

def isDark(img):
	'''
	Should only be called on color images
	'''
	gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	height, width = gray_image.shape
	total_pixels = height*width
	sum_brightness = sum(gray_image[i,j] for i in range(height) for j in range(width))
	return (sum_brightness/total_pixels) < 80

def split(file, grayscale = False):
	images = []
	image_type = 0 if grayscale else 1
	img = cv2.imread(file, image_type)
	if img.ndim == 2:
		img = np.expand_dims(img, axis=2)
		dark = True
	else:
		dark = isDark(img)
	height, width, channels = img.shape
	x,y = 0,0
	while(y < height):
		while(x < width):
			if(y+128>=height and x+128>=width):
				tmp = np.zeros((height-y, width-x, channels))
				tmp[:,:,:] = img[y:,x:,:]
				images.append(fill(tmp, dark))
			elif(y+128>=height):
				tmp = np.zeros((height-y, 128, channels))
				tmp[:,:,:] = img[y:,x:x+128,:]
				images.append(fill(tmp,dark))
			elif(x+128>=width):
				tmp = np.zeros((128, width-x, channels))
				tmp[:,:,:] = img[y:y+128,x:,:]
				images.append(fill(tmp,dark))
			else:
				tmp = np.zeros((128,128,channels))
				tmp[:,:,:] = img[y:y+128,x:x+128,:]
				images.append(tmp)
			x += 128
		y += 128
	return images


if __name__ == "__main__":
	print(split("./images/img3/images/00ae65c1c6631ae6f2be1a449902976e6eb8483bf6b0740d00530220832c6d3e.png", False))