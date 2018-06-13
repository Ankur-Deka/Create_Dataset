from Split_Images import split_images

images_path = '/media/ankur/UBUNTU 16_0/maps'	# Path to images
s_ext = 'pgm'		# The required images are .pgm files inside the folder and it's subfolders
store_path = './dataset'	# Path to store the resulting images
dest_ext = 'png'
num_augment=10000	# create 10,000 augmented images
[h,w]=[160,160]

my_splitter=split_images(images_path,store_path,s_ext,dest_ext,h,w)
my_splitter.split()
my_splitter.augment(num_augment)