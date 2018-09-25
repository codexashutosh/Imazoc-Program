'''
.
.
ATTENTION!
Before executing the program make sure that the image name "sample.jpeg" i.e. used in this program, must be replaced by the name of your sample/test image and the image and this program must be put inside the same directory.
.
.
'''
import sys
import imageio
import numpy as np
from PIL import Image, ImageTk, ImageOps

def createGreyList():
	im = Image.open('AsAtAn.jpeg')    # Replace sample.jpeg with the name of your sample/test image
	myGreyscale = im.convert('L')
	myGreyscale.save('sample_greyscale.jpeg','JPEG')
	im = Image.open('sample_greyscale.jpeg')
	im_array2 = np.asarray(im).tolist()
	return im_array2

#_________________________________________________________________________________________________

def createBlockArray(im_array2):
	im_array2.insert(0,[0 for _ in range(len(im_array2[0]))])
	im_array2.append([0 for _ in range(len(im_array2[0]))])
	width = len(im_array2[0])
	height = len(im_array2)
	blocks = []
	for i in range(0, height - slice_y + 1):
		blocks.append(
			[
				[0, im_array2[a][0], im_array2[a][1]]
				for a in range(i, i + slice_y)
			]
		)
		for j in range(0, width - slice_x + 1):
			blocks.append(
				[
					[im_array2[a][b] for b in range(j, j + slice_x)]
					for a in range(i, i + slice_y)
				]
			)
		blocks.append(
			[
				[im_array2[a][width-2], im_array2[a][width-1],0]
				for a in range(i, i + slice_y)
			]
		)
	return blocks

#_________________________________________________________________________________________________

def medianMode(blockArrayNp,im_array2):
	lst = []
	lst2 = []
	lst3 = []
	for i in range(len(blockArrayNp)):
		lst.append(
			[blockArrayNp[i][a][b] for a in range(slice_y) for b in range(slice_x)]
		)
	for blockValues in lst:
		lst2.append(int(sorted(blockValues)[int((len(blockValues)-1)/2)]))
	for i in range(0,len(lst2),len(im_array2[0])):
		lst3.append(
			[lst2[j] for j in range(i, i+len(im_array2[0]))]
		)
	lst3np = np.asarray(lst3)
	lst3np = lst3np.astype(np.uint8)
	return lst3np
		
#_________________________________________________________________________________________________

def minMode(blockArrayNp,im_array2):
	lst = []
	lst2 = []
	lst3 = []
	for i in range(len(blockArrayNp)):
		lst.append(
			[blockArrayNp[i][a][b] for a in range(slice_y) for b in range(slice_x)]
		)
	for blockValues in lst:
		lst2.append(int(min(blockValues)))
	for i in range(0,len(lst2),len(im_array2[0])):
		lst3.append(
			[lst2[j] for j in range(i, i+len(im_array2[0]))]
		)
	lst3np = np.asarray(lst3)
	lst3np = lst3np.astype(np.uint8)
	return lst3np
#_________________________________________________________________________________________________

def maxMode(blockArrayNp,im_array2):
	lst = []
	lst2 = []
	lst3 = []
	for i in range(len(blockArrayNp)):
		lst.append(
			[blockArrayNp[i][a][b] for a in range(slice_y) for b in range(slice_x)]
		)
	for blockValues in lst:
		lst2.append(int(max(blockValues)))
	for i in range(0,len(lst2),len(im_array2[0])):
		lst3.append(
			[lst2[j] for j in range(i, i+len(im_array2[0]))]
		)
	lst3np = np.asarray(lst3)
	lst3np = lst3np.astype(np.uint8)
	return lst3np
#_________________________________________________________________________________________________

def noiseSmMode(blockArrayNp,im_array2):
	lst = []
	lst2 = []
	lst3 = []
	for i in range(len(blockArrayNp)):
		lst.append(
			[blockArrayNp[i][a][b] for a in range(slice_y) for b in range(slice_x)]
		)
	for blockValues in lst:
		lst2.append(int(round(sum(blockValues)/len(blockValues))))
	for i in range(0,len(lst2),len(im_array2[0])):
		lst3.append(
			[lst2[j] for j in range(i, i+len(im_array2[0]))]
		)
	lst3np = np.asarray(lst3)
	lst3np = lst3np.astype(np.uint8)
	return lst3np

#_________________________________________________________________________________________________

if __name__=="__main__":
	print("\n")
	print("\t _________________________________________________________________________________________")
	print("\t|_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_|")
	print("\t|_|    _________________                                                                |_|")
	print("\t|_|   /                /                                                                |_|")
	print("\t|_|  /_____      _____/                                                                 |_|")
	print("\t|_|        |    |                                                                       |_|")
	print("\t|_|        |    |                                                                       |_|")
	print("\t|_|        |    |        ______      _______   _________    _______  ________   _____   |_|")
	print("\t|_|        |    |       /      \    /       | /         |  /      / /        \ /     \  |_|")
	print("\t|_|        |    |      /        \  /        |/  _____   | /__    / |   ____   |   ____| |_|")
	print("\t|_|   _____|    |_____/    /\    \/    /|   |  |     |  |   /   /  |  |    |  |  |      |_|")
	print("\t|_|  /               /    /  \        / |   |  |_____|  |__/   /___|  |____|  |  |_____ |_|")
	print("\t|_| /_______________/____/    \______/  |___|\____________/_______/ \________/ \______/ |_|")
	print("\t|_|_____________________________________________________________________________________|_|")
	print("\t|_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_                       _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_|")
	print("\t|_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_ WELCOME TO IMAZOC 1.0 _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_|")
	print("\t|_________________________________________________________________________________________|")
	print("\n\t Initiated IMAZOC 1.0 Program...\n")
	print("\t Initializing parameters... This may take some time depending on your processor...",end="   ")
	slice_x = 3
	slice_y = 3
	im_array2 = createGreyList()
	blockArray = createBlockArray(im_array2)
	blockArrayNp = np.array([np.array(row) for row in blockArray])
	print("DONE!\n")
	print("\t Initiated Median masking...",end="       						     ")
	blockArrayNpModMed = medianMode(blockArrayNp,im_array2)	# Median Masking
	imageio.imwrite('testMed.jpeg',blockArrayNpModMed)
	print("DONE!\n")
	print("\t Initiated Min masking...",end="          						     ")
	blockArrayNpModMin = minMode(blockArrayNp,im_array2)	    # Min Masking
	imageio.imwrite('testMin.jpeg',blockArrayNpModMin)
	print("DONE!\n")
	print("\t Initiated Max masking...",end="          						     ")
	blockArrayNpModMax = maxMode(blockArrayNp,im_array2)	    # Max Masking
	imageio.imwrite('testMax.jpeg',blockArrayNpModMax)
	print("DONE!\n")
	print("\t Initiated Noise smoothening...",end="    						     ")
	blockArrayNpModNSm = noiseSmMode(blockArrayNp,im_array2)	# Noise Smoothening
	imageio.imwrite('testNSm.jpeg',blockArrayNpModNSm)
	print("DONE!\n")
	print("\t Image Processing completed! Check the results in the parent folder. Thank You :)\n")
