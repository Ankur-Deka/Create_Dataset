# Class to create dataset from obstacle map (obtained from laser scan images)
# Works with only grayscale images now and supports data augmentation
# By Ankur Deka
# Date: 12th June, 2018

import numpy as np
import os
import pickle
import matplotlib.pyplot as plt
import time
import Augmentor

class split_images():
	# Class to create dataset
	# images_path: directory (and its sub directories) to look for
	# store_path: store directory
	# s_ext: extention of source images
	# dest_ext: extention to be sued for saving
	# [h,w]: required dimensions of image
	
	def __init__(self,images_path,store_path,s_ext,dest_ext,h,w):
		self.images_path=images_path
		self.store_path=store_path
		self.s_ext=s_ext
		self.dest_ext=dest_ext
		self.h=h
		self.w=w

	# Function to do the dividing job on one image
	def split_img(self,img,counter):
		[H,W]=img.shape
		Y=int(H/self.h)
		X=int(W/self.w)
		for y in range(Y):
			for x in range(X):
				h=self.h
				w=self.w
				array=img[y*h:(y+1)*h,x*w:(x+1)*w]				
				# Discard completely uniform images because there were a lot of them
				if array.max()-array.min()>0:
					# Augment if asked
					path=self.store_path+'/'+str(counter)
					plt.imsave(fname=path+'.'+self.dest_ext,arr=array,cmap='gray',format=self.dest_ext)
					counter+=1
		return counter		

	def augment(self,num_augment):
		print('Starting Augmentation')
		time_start=time.clock()
		p = Augmentor.Pipeline(self.store_path)
		# Point to a directory containing ground truth data.
		# Images with the same file names will be added as ground truth data
		# and augmented in parallel to the original data.
		# Add operations to the pipeline as normal:
		p.rotate(probability=0.7, max_left_rotation=25, max_right_rotation=25)
		p.flip_left_right(probability=0.7)
		p.flip_top_bottom(probability=0.7)
		p.zoom(probability=1, min_factor=1, max_factor=1)
		p.sample(num_augment)
		time_end=time.clock()
		print("\nFinished augmenting and saving in {} seconds".format(time_end-time_start))

	def split(self):
		# create the destination folder
		if not os.path.exists(self.store_path):
			os.makedirs(self.store_path)

		# Walk through the path and process the .pgm files
		print('Splitting')
		time_start=time.clock()
		counter = 0
		for path, subdirs, files in os.walk(self.images_path):
			for file in files:
				if file.endswith(self.s_ext):
					# we can now access all s_ext files one by one
					file_loc=os.path.join(path,file)
					img=plt.imread(file_loc)
					counter=self.split_img(img,counter)	
		time_end=time.clock()
		print("Finished Splitting and saving in {} seconds".format(time_end-time_start))