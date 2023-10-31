#program to capture single image from webcam in python

#importing OpenCV library
import cv2

#initialize the camera connected with current device, assign a value in cam_port variable according to that
cam_port = 0
cam = cv2.VideoCapture(cam_port) 

#reading the input using the camera
result, image = cam.read()


#If image will detected without any error show result
if result:

    #showing result, it take frame name and image output
    cv2.imshow("GeeksForGeeks", image)

    #saving image in local storage
    cv2.imwrite("GeeksForGeeks.png", image)

    #If keyboard interruptt occurs, destroy image
    #window
    cv2.waitKey(0)
    cv2.destroyWindow("GeeksForGeeks")
    #imwrite()
#If captured image is curroupted, moving to else part
else:
    print("No image detected, Please! try againg")