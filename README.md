# 🏫 Face Recognition Attendance System
## 📚 Table of Contents
Introduction
Features
Technologies Used
Installation
Usage
Code Explanation
Contributing
License
## 📖 Introduction
The Face Recognition Attendance System is a real-time application that utilizes face recognition technology to track attendance automatically. It captures video input, recognizes faces from a pre-defined list of students, and logs their attendance in a CSV file. This project enhances efficiency in attendance management and reduces manual errors.

## 🚀 Features
Real-time face recognition using a webcam.
Attendance logging in a CSV format with timestamps.
User-friendly interface displaying recognized names.
Capability to manage multiple known faces.
## 🛠️ Technologies Used
Python
OpenCV
Face Recognition (face_recognition library)
NumPy
CSV
DateTime
📥 Installation
To set up this project locally, follow these steps:

Clone the Repository:

``` bash
Copy code
git clone https://github.com/yourusername/face-recognition-attendance.git
cd face-recognition-attendance
Install Required Packages: Make sure you have Python installed, then install the necessary libraries:
```
``` bash
Copy code
pip install opencv-python face_recognition numpy
Prepare Face Images: Create a directory named faces and add images of known individuals you want to recognize, named appropriately (e.g., shashank.jpg, harry.png).
```
🏁 Usage
Run the application:

bash
Copy code
python attendance.py
The webcam will activate, and the program will start recognizing faces.

When a recognized face is detected, the video feed displays the name along with a "Present" message.

The attendance will be logged in a CSV file named after the current date.

## 📝 Code Explanation
The program captures video input using OpenCV.
It loads known face encodings from image files.
It detects faces and compares each frame captured with the known encodings.
If a match is found, the student's name is displayed and logged in a CSV file.

## 🔑 Key Components
Face Recognition: Utilizes face_recognition library for detecting and encoding faces.
Attendance Logging: Logs the name and time of presence in a CSV file.
Real-time Video Capture: OpenCV is used to display the video feed and recognize faces.
