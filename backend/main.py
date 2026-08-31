#back main.py
import os
import cv2
import threading
import time
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse


app = FastAPI()


state = {
    "x": 0,
    "y": 0,
    "kp": 0,
    "ki": 0,
    "kd": 0
}

MODE = os.getenv("MODE", "SIM")  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# iniciar thread DEPOIS do state
if MODE == "SIM":
    from simulator import run_simulation
    threading.Thread(target=run_simulation, args=(state,), daemon=True).start()

elif MODE == "PC":
    from camera_pc import run_camera
    threading.Thread(target=run_camera, args=(state,), daemon=True).start()

elif MODE == "RASPI":
    from camera import run_camera
    threading.Thread(target=run_camera, args=(state,), daemon=True).start()

# modelo PID
class PID(BaseModel):
    kp: float
    ki: float
    kd: float


# 🔹 rota posição
@app.get("/position")
def get_position():
    return {"x": state["x"], "y": state["y"]}


# 🔹 rota receber PID
@app.post("/pid")
def set_pid(pid: PID):
    state["kp"] = pid.kp
    state["ki"] = pid.ki
    state["kd"] = pid.kd
    return {"msg": "PID atualizado"}

@app.get("/video")
def video_feed():
    return StreamingResponse(generate_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame")

def generate_frames():
    while True:
        if "frame" not in state:
            time.sleep(0.05)
            continue

        frame = state["frame"]

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

        time.sleep(0.03)  # ~30 FPS