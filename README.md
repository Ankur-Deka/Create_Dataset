# Create_Dataset
Generic Module for Creating Image Dataset. Can split  given images into smaller images and/or perform data augmentation.

Requirements:
1) Augmentor: pip install Augmentor

Supports:
1) Gray Scale Images
2) Data augmentation

Input:
1) Path to directory. Images will be searched in this directorry and its sub directories
2) Input image format
3) Output Image format
4) Required output image size
5) Number of output images after augmentation

Output:
1) Splitted images
2) Augmented images if augmentation is asked for

Refer to file create_dataset.py for usage
