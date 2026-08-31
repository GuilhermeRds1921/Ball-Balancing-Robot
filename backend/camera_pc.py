import cv2
import numpy as np

def run_camera(state):
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("ERRO: câmera não abriu")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        # 🔹 detecção HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 🔴 faixa 1 (vermelho baixo)
        lower1 = np.array([0, 120, 70])
        upper1 = np.array([10, 255, 255])

        # 🔴 faixa 2 (vermelho alto)
        lower2 = np.array([170, 120, 70])
        upper2 = np.array([180, 255, 255])

        mask1 = cv2.inRange(hsv, lower1, upper1)
        mask2 = cv2.inRange(hsv, lower2, upper2)

        mask = mask1 + mask2

        # 🔹 limpeza
        mask = cv2.GaussianBlur(mask, (5, 5), 0)
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)

        # 🔹 contornos (AGORA DENTRO DO LOOP)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            c = max(contours, key=cv2.contourArea)

            if cv2.contourArea(c) > 300:
                (x, y), radius = cv2.minEnclosingCircle(c)

                state["x"] = int(x)
                state["y"] = int(y)

                # desenhar
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
                cv2.circle(frame, (int(x), int(y)), 5, (0, 0, 255), -1)

        # 🔹 salvar frame DEPOIS do desenho
        state["frame"] = frame