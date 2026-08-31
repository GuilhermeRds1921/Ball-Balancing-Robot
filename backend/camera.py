#back camera.py
from picamera2 import Picamera2
import cv2
import numpy as np

def run_camera(state):
    picam2 = Picamera2()

    config = picam2.create_preview_configuration(
        main={"size": (640, 480)}
    )
    picam2.configure(config)
    picam2.start()

    while True:
        frame = picam2.capture_array()

        # 🔹 salvar frame para streaming
        state["frame"] = frame

        # 🔹 converter para HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 🔴 ajustar depois
        lower = np.array([0, 120, 70])
        upper = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, lower, upper)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            c = max(contours, key=cv2.contourArea)

            if cv2.contourArea(c) > 300:
                (x, y), radius = cv2.minEnclosingCircle(c)

                state["x"] = int(x)
                state["y"] = int(y)

                # 🔹 desenhar no frame
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
                cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)