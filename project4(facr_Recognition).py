import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)  

# Load known faces
def load_face(file_path):
    image = face_recognition.load_image_file(file_path)
    return face_recognition.face_encodings(image)[0]

known_face_encodings = [
    load_face("faces/shashank.jpg"),
    load_face("faces/harry.png")
]
known_face_names = ["shashank", "harry"]

# List of expected students
students = known_face_names.copy()

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")
csv_file_name = f"{current_date}.csv"

# Open CSV file with header
with open(csv_file_name, "w+", newline="") as f:
    lnwriter = csv.writer(f)
    lnwriter.writerow(["Name", "Time"])  # Header

    while True:
        # Capture frame-by-frame
        _, frame = video_capture.read()
        
        # Resize the frame to 1/4 size for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Find all face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            # Compare face encoding with known face encodings
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distance)
            
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                if name in known_face_names:
                
                    # Display name and 'Present' on the frame
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    bottom_left_corner_of_text = (10, 100)
                    font_scale = 1.5
                    font_color = (255, 0, 0)
                    thickness = 3
                    line_type = cv2.LINE_AA
                    
                    cv2.putText(frame, f"{name} Present", bottom_left_corner_of_text, font, font_scale, font_color, thickness, line_type)
                    
                # Log attendance if the student is in the list
                    if name in students:
                        students.remove(name)
                        current_time = datetime.now().strftime("%H-%M-%S")
                        lnwriter.writerow([name, current_time])
            
        # Display the resulting frame
        cv2.imshow("Attendance", frame)
        
        # Exit the loop with 'q' key
        if cv2.waitKey(1) & 0xFF == ord("s"):
            break

# Release the video capture and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
