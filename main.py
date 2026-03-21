import cv2
import pyttsx3
import time
import threading
from ultralytics import YOLO

# ------------------ LOAD MODEL --------------
# ---
model = YOLO("best.pt")

# ------------------ CONTROL VARIABLES ------------------
last_spoken = ""
cooldown = 2  # seconds
last_time = 0

# ------------------ SPEAK FUNCTION (NON-BLOCKING) ------------------
def speak_task(text):
    try:
        # Initialize engine inside thread for safety
        temp_engine = pyttsx3.init()
        temp_engine.setProperty('rate', 140)
        temp_engine.setProperty('volume', 1.0)
        temp_engine.say(text)
        temp_engine.runAndWait()
    except Exception as e:
        print(f"Voice Error: {e}")

def speak(text):
    threading.Thread(target=speak_task, args=(text,), daemon=True).start()

# ------------------ CAMERA ------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not working ❌")
    exit()

print("Camera started... Press ESC to exit")

# ------------------ MAIN LOOP ------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # YOLO Prediction
    results = model(frame)

    current_time = time.time()

    for r in results:
        if r.boxes is not None:
            for box in r.boxes:

                cls_id = int(box.cls[0])
                label = model.names[cls_id]

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Draw rectangle
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)

                # Put text
                cv2.putText(frame, label.upper(), (x1, y1-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

                # Voice output (with cooldown)
                if (label != last_spoken) or (current_time - last_time > cooldown):
                    print("Speaking:", label)
                    speak(label)

                    last_spoken = label
                    last_time = current_time

    cv2.imshow("Sign Language AI (YOLO + Voice)", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC key
        break

# ------------------ CLEANUP ------------------
cap.release()
cv2.destroyAllWindows()