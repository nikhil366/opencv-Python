import cv2
import numpy as np

'''
create a function that take input of height and width and colour 
combination according to user requirement
'''
def create_image(height, width, color_rgb = (0,0,0)):
    '''Create image according to our given colour'''
    image = np.zeros((height, width, 3), np.uint8)
    color = tuple(reversed(color_rgb))
    image[:] = color
    return image

# here our function is created, now we can create a image using numpy zeroes according to 
# our colour requirements
height1, width1 = 512, 512

colr = (124,122,32)
image = create_image(height1, width1, color_rgb=colr)
cv2.imshow("Blank Image", image)
cv2.imwrite('red.jpg', image)
cv2.waitKey(0)
cv2.destroyAllWindows()