import cv2

from utils import get_limits
from PIL import Image

yellow = [0, 255, 255] #represents yellow in bgr color space 
green = (0, 255, 0)
red = [0, 0, 255]

cap = cv2.VideoCapture(1) #begins the video capture on mac camera (specifies the camera that we load)
#hsv color space: hue (the color > different colors have different hues), saturation, and value 
#telling program to detect all pixes within the yellow hue region (define a region)

while True:
    ret, frame = cap.read() #read frames  

    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #coverts the images from the rgb color space to the hsv color space

    lower_limit, upper_limit = get_limits(color=yellow)

    #gets all the pixels in the frame that are within the color range 
    mask = cv2.inRange(hsvImage, lower_limit, upper_limit) #returns a "mask" of things that are in this color range 
    #if we were to visualize the mask, it would be a dark screen with light where the color yellow is in the frame 

    mask_ = Image.fromarray(mask) #coverting the image from numpy (in CV) to pillow 

    bbox = mask_.getbbox() #gets the bounding box for this 

    if bbox is not None:
        x1, y1, x2, y2 = bbox #converts the bounding box to its coordinates
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), green, 5) 
        #draws rectangle on the original frame by specifying top left corner and bottom right corner 
        #choose color to draw in + thickness of the lines 

    cv2.imshow('frame', frame) #visualize the frame 

    if cv2.waitKey(1) & 0xFF == ord('q'): #quits the application if q is pressed 
        break


cap.release()


cv2.destroyAllWindows()