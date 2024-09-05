# Intrusion Detection System using OpenCV

This project implements a basic Intrusion Detection System using OpenCV in Python. It detects motion from a camera feed (webcam or video file) and flags it as a potential intrusion by drawing bounding boxes around detected objects.

## Features
- Real-time motion detection via camera feed.
- Highlights areas of motion with bounding boxes.
- Alerts with an "Intrusion Detected!" message when movement is detected.
  
## Requirements
- Python 3.x
- OpenCV Library

## Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/intrusion-detection.git
Install required packages: Install OpenCV if you haven't already:


Copy code
pip install opencv-python
Run the script: Navigate to the project directory and run the Python script:


Copy code
python intrusion_detection.py

Usage
Live Camera Feed: The default script uses the primary webcam for motion detection.
Video File Input: To test with a video file, modify the following line in the code:
python

Copy code
camera = cv2.VideoCapture('path_to_your_video_file.mp4')

How it Works
The system compares the first frame of the camera feed (background) to subsequent frames.
Significant differences between the frames (motion) trigger the detection, and a bounding box is drawn around the moving object.
The motion-detection threshold can be adjusted in the code to control sensitivity.

Keyboard Shortcuts
q: Press q to quit the program.

Future Enhancements
Add email or SMS alerts upon detection.
Implement recording of detected motion clips.
Integrate a more advanced object recognition model.

License
This project is licensed under the MIT License. See the LICENSE file for more information.

This **README** provides a clear overview of the project, setup instructions, usage, and future possibilities. You can customize it further as needed.
