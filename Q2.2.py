import time
import cv2
  
image = cv2.imread('D:/Documents/Pictures/bird2.png')
start_time = time.time()
grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
cv2.imwrite("graybird.png",grayimage)
print("--- %s seconds ---" % (time.time() - start_time))

