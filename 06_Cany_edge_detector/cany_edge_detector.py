'''Cany edge detector is a edge detection operator that use multi stage algoritham to detect 
the wide ranges of edges in a image
cany edge detection is divided in 5 steps these are :
1. noise reduction (apply gaussian filter)
2. Gradient calculation
3. non maximum supersion
4. Double threshold
5. edge tracking by Hysteresis

this is seems very complicated but we can apply it very easily in computer vision
with method canny()
'''
import cv2 
from matplotlib import pyplot as plt

def nothing(x):
    print(x)

image_path = ('/home/nikhil/Desktop/Data/ni.jpg')
image = cv2.imread(image_path, 0)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)



cannny = cv2.Canny(image,100,200)
# here Hysteresis threshold value is provided



titles = ['image_nr','cannny']
images = [image,cannny]

for i in range(2):
    plt.subplot(1,2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])

plt.show()