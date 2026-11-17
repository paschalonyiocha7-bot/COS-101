# STUDENT 5 - PHYSICS CALCULATOR

def average_velocity():
    displacement = float(input("Enter displacement: "))
    time = float(input("Enter time: "))
    if time > 0:
        print("Average Velocity =", displacement / time, "m/s")
    else:
        print("Invalid time")

def distance():
    velocity = float(input("Enter velocity: "))
    time = float(input("Enter time: "))
    print("Distance =", velocity * time, "meters")

def displacement():
    u = float(input("Enter initial velocity: "))
    time = float(input("Enter time: "))
    acceleration = float(input("Enter acceleration: "))
    result = u * time + 0.5 * acceleration * time ** 2
    print("Displacement =", result, "meters")

def torque():
    force = float(input("Enter force: "))
    distance = float(input("Enter perpendicular distance: "))
    print("Torque =", force * distance, "Nm")

def mechanical_advantage():
    load = float(input("Enter load: "))
    effort = float(input("Enter effort: "))
    if effort != 0:
        print("Mechanical Advantage =", load / effort)
    else:
        print("Effort cannot be zero")

while True:
    print("\n===== PHYSICS CALCULATOR =====")
    print("1. Average Velocity")
    print("2. Distance")
    print("3. Displacement")
    print("4. Torque")
    print("5. Mechanical Advantage")

    choice = input("Choose an operation (1-5): ")

    if choice == "1":
        average_velocity()
    elif choice == "2":
        distance()
    elif choice == "3":
        displacement()
    elif choice == "4":
        torque()
    elif choice == "5":
        mechanical_advantage()
    else:
        print("Invalid choice")

    repeat = input("Do you want to calculate again? (yes/no): ")
    if repeat.lower() != "yes":
        print("Thank you!")
        break
