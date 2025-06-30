# WRO-Project
Has details about our journey in WRO
## 🔧 Hardware Overview

- Jetson Nano B01 (4GB)
- Pololu 37D DC Motor (FWD)
- Cytron MD10C Motor Driver
- MG996R Servo Motor for Steering
- PCA9685 PWM Controller
- HC-SR04 Ultrasonic Sensor ×2
- CSI Camera (Raspberry Pi V2)
- TCS34725 Color Sensor
- BNO055 IMU
- Turnigy 2S 2200mAh LiPo Battery + UBEC (5V/5A)

---

## 🧠 Vision & Control Strategy

- *Lane Detection*: Edge detection + curve fitting
- *Traffic Signs*: Color + shape recognition for red/green
- *Obstacle Handling*: HC-SR04 with stop-and-wait + camera CV backup
- *Parking Logic*: Detect magenta zone, align with ultrasonic
- *Lap Counting*: Planned via zone detection or color markers

---

## 📂 Repository Structure
├── main.py
├── hardware_interfaces.py
├── ultrasonic_obstacle_avoidance.py
├── parking_lot_detection.py
├── TODO.md
├── journal.md (to be added)
├── README.md
