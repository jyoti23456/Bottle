import cv2
import numpy as np
from ultralytics import YOLO 

model = YOLO("yolov5s.pt")

trajectory = []
prev_orientation = None

cap = cv2.VideoCapture(0)
   
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, conf=0.5)
    bottles = results[0].boxes

        confidence = box.conf[0].item()

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        center = ((x1 + x2) // 2, (y1 + y2) // 2)
        trajectory.append(center)

        width = x2 - x1
        height = y2 - y1
        orientation = "Upright" if height > width * 2 else "Horizontal"

        if prev_orientation != orientation:
            prev_orientation = orientation
            print(f"Bottle orientation changed: {orientation}")

        for i in range(1, len(trajectory)):
            if trajectory[i - 1] is None or trajectory[i] is None:
                continue
            cv2.line(frame, trajectory[i - 1], trajectory[i], (0, 255, 255), 2)

        if len(trajectory) > 2:
            dy = trajectory[-1][1] - trajectory[0][1]
            if dy < 0 and orientation == "Upright":
                cv2.putText(frame, "Flip Detected!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                print("Bottle flip detected!")

    cv2.imshow("Bottle Flip Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()