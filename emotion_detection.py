#================================================================human emotion detector code
# Import necessary libraries
import cv2
import numpy as np

# Load pre-trained face and emotion detection models
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
emotion_model = cv2.dnn.readNetFromTensorflow('emotion_model.pb')

# Define a list of emotion labels
emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']

# Start capturing video from the default camera
cap = cv2.VideoCapture(0)

while True:
    # Read each frame from the video feed
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the frame to grayscale for face detection
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract the face region from the frame
        face_roi = gray_frame[y:y + h, x:x + w]

        # Preprocess the face region for emotion prediction
        face_blob = cv2.dnn.blobFromImage(face_roi, 1.0, (48, 48), (0, 0, 0), swapRB=True, crop=False)
        emotion_model.setInput(face_blob)

        # Make the emotion prediction
        emotions_preds = emotion_model.forward()
        emotion_index = np.argmax(emotions_preds)
        emotion_label = emotion_labels[emotion_index]

        # Display the predicted emotion on the frame
        cv2.putText(frame, emotion_label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with emotion labels
    cv2.imshow('Emotion Detector', frame)

    # Exit the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()
