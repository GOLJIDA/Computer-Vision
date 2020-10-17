import cv2
import face_recognition


# Capture video
video_capture = cv2.VideoCapture(0)
# List for storing boxes coordinates of faces
face_locations = []

while True:
    # Get retval and frame
    ret, frame = video_capture.read()
    # Get array that forms square where faces are detected
    face_locations = face_recognition.face_locations(frame)
    # Draw squares around faces
    for top, right, bottom, left in face_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    # Draw window with our frame
    cv2.imshow('How to funk', frame)
    # Handler for exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Stop retrieving frames
video_capture.release()
# Close all windows
cv2.destroyAllWindows()
