# ultrasonic_obstacle_avoidance.py

from hardware_interfaces import get_distance, set_motor, set_steering
import time

def avoid_obstacle():
    dist = get_distance()
    print(f"[Ultrasonic] Distance: {dist} cm")

    if dist < 20:
        print("Obstacle detected! Stopping.")
        set_motor(0)
        time.sleep(1)
    else:
        set_motor(50)  # Forward with medium speed
        set_steering(90)  # Straight ahead
