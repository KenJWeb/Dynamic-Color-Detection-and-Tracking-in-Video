Color Detection in Video
This project is a Python-based application that detects specific colors in a video or live webcam feed. It uses OpenCV and PIL (Pillow) libraries to process the video frames and highlight the selected color in real-time. The program allows users to choose between a pre-recorded video, a live webcam feed, or a custom video file, and then select a color to detect (blue, yellow, green, or red).

Features
Detect specific colors in a video or live webcam feed.

Draw bounding boxes around detected objects of the selected color.

Supports pre-recorded videos, live webcam feeds, and custom video files.

Easy-to-use command-line interface for selecting video source and color.

Requirements
To run this project, you need the following Python libraries:

opencv-python

Pillow

You can install these libraries using pip:

bash
Copy
pip install opencv-python
pip install Pillow
How to Use
Clone this repository or download the script.

Ensure you have the required libraries installed (see above).

Run the script using Python:

Follow the on-screen prompts:

Select the video source:

1: Use a pre-recorded video (video.mp4).

2: Use the live webcam feed.

3: Use a custom video file (my_video.mp4).

Select the color to detect:

1: Blue

2: Yellow

3: Green

4: Red

The program will display two windows:

frame: The original video with bounding boxes around detected objects.

mask: The binary mask showing the detected color.

Press q to exit the program.

Code Structure
The script uses OpenCV to capture video frames and convert them to the HSV color space for better color detection.

The colors function defines the lower and upper HSV bounds for each color.

Contours are used to detect objects of the selected color, and bounding boxes are drawn around them.

Example
Here’s an example of how to use the program:

Run the script.

Select 2 for the live webcam feed.

Select 1 to detect the color blue.

The program will highlight blue objects in the webcam feed with green bounding boxes.

Notes
Ensure the video file (video.mp4 or my_video.mp4) is in the same directory as the script if you choose options 1 or 3.

The color detection is based on HSV values, which may need adjustment depending on lighting conditions.

License
This project is open-source and available under the MIT License. Feel free to modify and distribute it as needed.
