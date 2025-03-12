import cv2
from PIL import Image
import numpy as np
from limits import colors

# choosing video
print("Select video:")
print("1: Video with crowd")
print("2: Live webcam")
print("3: My video")
choice = input("Enter your choice (1 - 3): ")

if choice == "1":

    video_path = "video.mp4"
    cap = cv2.VideoCapture(video_path)

elif choice == "2":

    cap = cv2.VideoCapture(0)

elif choice == "3":

    video_path = "my_video.mp4"
    cap = cv2.VideoCapture(video_path)

else:
    print("Invalid choice. Exiting.")
    exit()

# choose color
print("Select color to detect:")
print("1: Blue")
print("2: Yellow")
print("3: Green")
print("4: Red")
color_choice = input("Enter your choice (1, 2, 3, or 4): ")

if color_choice == "1":
    lowerLimit, upperLimit = colors("blue")
elif color_choice == "2":
    lowerLimit, upperLimit = colors("yellow")
elif color_choice == "3":
    lowerLimit, upperLimit = colors("green")
elif color_choice == "4":
    lowerLimit, upperLimit = colors("red")
else:
    print("Invalid choice. Exiting.")
    exit()

while True:
    # read frames from camera
    ret, frame = cap.read()

    # converting RGB to Hsv
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # color detection from lower and upper bounds
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    # applying mask
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # convert the mask array numpy into pil image format
    mask_ = Image.fromarray(mask)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw rectangles around each detected object
    for contour in contours:
        if cv2.contourArea(contour) > 400:  # Filter out small objects
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()