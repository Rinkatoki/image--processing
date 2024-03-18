import cv2

def edge_detection():
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, 50, 150)
    cv2.imshow("Edges",edges)
    cv2.waitKey(0)
    plt.show()
    
def image_rotation():
    image = cv2.rotate(original_image, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow("image",image)
    cv2.waitKey(0)

def gray_scaling():
    gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    cv2.imshow("grey image",gray_image)
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
