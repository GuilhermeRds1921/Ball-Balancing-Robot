import random
import time

def run_simulation(state):
    while True:
        state["x"] = random.randint(0, 640)
        state["y"] = random.randint(0, 480)
        time.sleep(0.2)