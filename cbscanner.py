import cv2
from roboflow import Roboflow  

# Initialize Roboflow and load model
rf = Roboflow(api_key="LtOWijXg0XxaIFvnHuZo")
model = rf.workspace().project("philippine-money-nbgvl-rgoa8").version(1).model

# Define label-to-value mapping
value_map = {
    "1": 1, "5": 5, "10": 10, "20": 20, 
    "50": 50, "100": 100, "200": 200, 
    "500": 500, "1000": 1000
}

# Open the camera feed
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Save the current frame as a temporary image file
    temp_image_path = "temp_frame.jpg"
    cv2.imwrite(temp_image_path, frame)

    # Perform prediction
    response = model.predict(temp_image_path, confidence=70, overlap=30).json()

    # Initialize sum
    sum = 0

    # Process predictions
    for pred in response['predictions']:
        x, y, w, h = int(pred['x']), int(pred['y']), int(pred['width']), int(pred['height'])
        label = pred['class']
        sum += value_map.get(label, 0)
        
        # Draw bounding box and label
        start, end = (x - w // 2, y - h // 2), (x + w // 2, y + h // 2)
        cv2.rectangle(frame, start, end, (0, 255, 0), 2)
        cv2.putText(frame, label, (start[0], start[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2)

    # Display the sum on the frame
    cv2.putText(frame, f"Sum: PHP {sum}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Show the frame with bounding boxes and sum
    cv2.imshow("Real-Time Money Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()