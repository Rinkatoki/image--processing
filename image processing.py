import cv2
import numpy as np
from matplotlib import pyplot as plt

def edge_detection():
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, 50, 150)
    plt.subplot(121), plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)), plt.title('Original Image')
    plt.subplot(122), plt.imshow(edges, cmap='gray'), plt.title('Edge Detection')
    plt.show()
    
def image_rotation():
    image = cv2.resize(original_image, (0, 0), fx = 0.1, fy = 0.1)
    half = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("image", half)
    cv2.waitKey(0)

def gray_scaling():
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    half_gray = cv2.resize(gray_image, (0, 0),fx = 0.1,fy = 0.1)
    cv2.imshow("grey image",half_gray)
    cv2.waitKey(0)

    
image_root= 'D:\\Nexilo\\image--processing\\Edge_detect.jpg'
original_image = cv2.imread(image_root)
print("choose the option")
print("1.Edge detection")
print("2.Image rotaion")
print("3.Gray scaling")
n=int(input("Enter the option:"))
if (n==1):
    edge_detection()
elif(n==2):
    image_rotation()
elif(n==3):
    gray_scaling()
else:
    print("invalid option")
