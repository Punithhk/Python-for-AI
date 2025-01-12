import os.path
from skimage.io import imread
import time
img = imread(os.path.join('check.jpg'))

import matplotlib.pyplot as plt 

plt.imshow(img)

print(img)
print('Image properties : ',type(img), img.ndim,img.shape)

#slicing the image 
img_slice = img.copy()
img_slice = img_slice[0:300,360:480]
plt.figure()
plt.imshow(img_slice)
time.sleep(5)
# this will replace the space with black as value is 0
img[0:300,360:480,:] = 0
plt.imshow(img)
time.sleep(5)
#add the image back
img[0:300,360:480,:] = img_slice
plt.imshow(img)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  