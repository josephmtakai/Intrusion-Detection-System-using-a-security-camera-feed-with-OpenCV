import cv2

# Initialize camera feed (0 for default camera or the path to your video file)
camera = cv2.VideoCapture(0)

# Read the first frame to use as the background for motion detection
ret, frame1 = camera.read()
frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame1_gray = cv2.GaussianBlur(frame1_gray, (21, 21), 0)

# Continuously read camera feed
while camera.isOpened():
    ret, frame2 = camera.read()
    if not ret:
        break

    # Convert the frame to grayscale and blur to reduce noise
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    frame2_gray = cv2.GaussianBlur(frame2_gray, (21, 21), 0)

    # Compute the absolute difference between the first frame and the current frame
    frame_diff = cv2.absdiff(frame1_gray, frame2_gray)

    # Threshold the difference to create a binary image (highlight moving regions)
    thresh = cv2.threshold(frame_diff, 25, 255, cv2.THRESH_BINARY)[1]

    # Dilate the threshold image to fill in small holes
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Find contours (outlines) of the moving objects
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Ignore small contours (noise)
        if cv2.contourArea(contour) < 500:
            continue

        # Get the bounding box of the detected motion
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame2, "Intrusion Detected!", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Display the camera feed with detections
    cv2.imshow("Security Camera", frame2)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close windows
camera.release()
cv2.destroyAllWindows()
