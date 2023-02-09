import time

def pump1():
    print("Pompe 1")
    time.sleep(2)
    return 10

def pump2():
    print("Pompe 2")
    time.sleep(3)
    return 20

def machine1(oil):
    print("Machine 1")
    time.sleep(5)
    return max(0, oil - 25), 1 if oil >= 25 else 0

def machine2(oil):
    print("Machine 2")
    time.sleep(3)
    return max(0, oil - 5), 1 if oil >= 5 else 0

def watchdog():
    oil = 0
    motor_count = 0
    wheel_count = 0
    while True:
        oil += pump1() if oil < 50 else 0
        oil += pump2() if oil < 50 else 0
        oil = min(50, oil)
        if wheel_count // 4 < motor_count:
            oil, motor = machine1(oil)
            motor_count += motor
        else:
            oil, wheel = machine2(oil)
            wheel_count += wheel
        print("Huile: ", oil)
        print("Moteur: ", motor_count)
        print("Roue: ", wheel_count)
        time.sleep(5)
        oil += pump1() if oil < 50 else 0
        time.sleep(15)
        oil += pump2() if oil < 50 else 0
        oil = min(50, oil)
        if wheel_count // 4 < motor_count:
            oil, motor = machine1(oil)
            motor_count += motor
        else:
            oil, wheel = machine2(oil)
            wheel_count += wheel
        print("Huile: ", oil)
        print("Moteurs: ", motor_count)
        print("Roues: ", wheel_count)
        time.sleep(5)

if __name__ == "__main__":
    watchdog()
