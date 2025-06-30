# main.py

from ultrasonic_obstacle_avoidance import avoid_obstacle
from parking_lot_detection import detect_and_park
from hardware_interfaces import init_camera

import time

def main():
    cam = init_camera()

    print("Starting test loop. Running both modules...")
    
    for i in range(5):
        avoid_obstacle()
        ret, frame = cam.read()
        if ret:
            detect_and_park(frame)
        time.sleep(1)

    cam.release()
    print("Test complete.")

if __name__ == "__main__":
    main()
