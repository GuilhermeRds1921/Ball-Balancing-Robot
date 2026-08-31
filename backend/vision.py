from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from picamera2 import Picamera2
import cv2
import numpy as np
import threading

app = FastAPI()

# CORS (IMPORTANTE pro React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

state = {
    "x": 0,
    "y": 0,
    "kp": 0,
    "ki": 0,
    "kd": 0
}

class PID(BaseModel):
    kp: float
    ki: float
    kd: float


@app.get("/position")
def get_position():
    return {"x": state["x"], "y": state["y"]}


@app.post("/pid")
def set_pid(pid: PID):
    state["kp"] = pid.kp
    state["ki"] = pid.ki
    state["kd"] = pid.kd
    return {"message": "PID atualizado"}


# 🎥 THREAD DA CÂMERA + DETECÇÃO
def camera_loop():
    picam2 = Picamera2()
    config = picam2.create_preview_configuration(
        main={"size": (320, 240)}  # leve pro Pi 3
    )
    picam2.configure(config)
    picam2.start()

    while True:
        frame = picam2.capture_array()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # AJUSTAR PARA SUA BOLA
        lower = np.array([0, 120, 70])
        upper = np.array([10, 255, 255])

        mask = cv2.inRange(hsv, lower, upper)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            c = max(contours, key=cv2.contourArea)

            if cv2.contourArea(c) > 200:
                (x, y), radius = cv2.minEnclosingCircle(c)

                state["x"] = int(x)
                state["y"] = int(y)


# iniciar thread
threading.Thread(target=camera_loop, daemon=True).start()