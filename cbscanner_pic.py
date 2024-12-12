import cv2
from gtts import gTTS
import os
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

def process_predictions(response):
    """Process the predictions and calculate the total sum."""
    total_sum = 0
    for pred in response['predictions']:
        total_sum += value_map.get(pred['class'], 0)
    return total_sum

def play_text_to_speech(text, language='en'):
    """Generate and play text-to-speech."""
    tts = gTTS(text, lang=language)
    temp_file = '/tmp/temp.mp3'
    tts.save(temp_file)
    os.system(f'mpg321 {temp_file}')
    os.remove(temp_file)

def draw_bounding_boxes(frame, response):
    """Draw bounding boxes and labels on the image."""
    for pred in response['predictions']:
        x, y, w, h = int(pred['x']), int(pred['y']), int(pred['width']), int(pred['height'])
        label = pred['class']
        start, end = (x - w // 2, y - h // 2), (x + w // 2, y + h // 2)
        cv2.rectangle(frame, start, end, (0, 255, 0), 2)
        cv2.putText(frame, label, (start[0], start[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)

def main():
    image_path = "datasets/100_f.jpg"  # Provide the path to your image
    frame = cv2.imread(image_path)
    
    if frame is None:
        print("Error: Could not read the image.")
        exit()

    # Perform prediction
    response = model.predict(image_path, confidence=70, overlap=30).json()

    # Calculate total sum from predictions
    total_sum = process_predictions(response)

    # Generate and play speech
    play_text_to_speech(f'{total_sum} peso')

    # Display the sum on the image
    # cv2.putText(frame, f"Sum: PHP {total_sum}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Draw bounding boxes on the image
    draw_bounding_boxes(frame, response)

    # Show the processed image with bounding boxes and sum
    cv2.imshow("Money Detection Result", frame)

    # Wait for a key press to close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
