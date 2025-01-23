Bottle Flip Detection Using YOLO
This project uses the YOLOv5 model for real-time detection and tracking of bottles via a webcam feed. The application identifies the orientation of bottles (upright or horizontal), tracks their trajectory, and detects bottle flips.

Features
Real-time detection of bottles using the YOLOv5 model.
Tracks the trajectory of bottles and visualizes it on the video feed.
Identifies bottle orientation changes (e.g., upright or horizontal).
Detects bottle flips and displays a message when a flip is detected.
Requirements
To run this project, ensure you have the following dependencies installed:

Python Libraries
opencv-python
numpy
ultralytics
Hardware
A computer with a working webcam or an external camera.
Installation
Clone the Repository

bash
Copy
Edit
git clone https://github.com/jyoti23456/Bottle.git 
cd Bottle  
Install Dependencies
Use pip to install the required Python libraries:

bash
Copy
Edit
pip install opencv-python numpy ultralytics  
Download YOLOv5 Pretrained Weights
Ensure the YOLOv5 weights file (yolov5s.pt) is available in the project directory.

You can download it from the official Ultralytics GitHub page.
Usage
Run the Script
Start the real-time bottle detection by running the script:

bash
Copy
Edit
python bottle_flip.py  
Controls

Press q to quit the application.
How It Works
Bottle Detection:
The YOLOv5 model detects bottles in the video feed and draws bounding boxes around them.

Orientation Check:
Based on the bounding box dimensions, the script determines if the bottle is upright or horizontal.

Trajectory Tracking:
The center of the bottle's bounding box is tracked and connected with lines to show the movement trajectory.

Flip Detection:
If the trajectory indicates upward motion followed by an upright orientation, a flip is detected, and a message ("Flip Detected!") is displayed.

Sample Output
When running the script, you'll see:

A real-time video feed with bottles detected and tracked.
Bounding boxes around the bottles.
Trajectory lines showing the movement.
A notification if a bottle flip is detected.
Contributing
Feel free to contribute by submitting issues or pull requests. If you have suggestions for improvement, create a pull request or open an issue.

License
This project is licensed under the MIT License.

Acknowledgments
Ultralytics YOLOv5 for the object detection framework.
OpenCV for real-time video processing.
Let me know if you'd like further customization! 🚀
