from glob import glob
import cv2
import matplotlib.pyplot as plt
import numpy as np

def combine(image, masks, path):
	base = cv2.imread(image, 1)
	height, width, _ = base.shape
	canvas = np.zeros(shape = (height, width))
	for mask in masks:
		img = cv2.imread(mask, 0)
		for i in range(height):
			for j in range(width):
				if(img[i,j] == 255):
					canvas[i,j] = 255		
	cv2.imwrite(path, canvas)
	print(path, "written")


filepaths = glob('./images/*/')

for filepath in filepaths:
	path = filepath + "masks/*"
	image = filepath + "images/*"
	image = glob(image)[0]
	masks = glob(path)
	combine(image, masks, filepath + 'masks/full.jpg')
