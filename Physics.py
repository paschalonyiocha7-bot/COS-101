
def speed():
    distance = float(input("Enter distance in metres: "))
    time = float(input("Enter time in seconds: "))
    return distance / time


def force():
    mass = float(input("Enter mass in kg: "))
    acceleration = float(input("Enter acceleration in m/s²: "))
    return mass * acceleration


def weight():
    mass = float(input("Enter mass in kg: "))
    gravity = float(input("Enter gravitational acceleration: "))
    return mass * gravity


def kinetic_energy():
    mass = float(input("Enter mass in kg: "))
    velocity = float(input("Enter velocity in m/s: "))
    return 0.5 * mass * velocity ** 2


def potential_energy():
    mass = float(input("Enter mass in kg: "))
    gravity = float(input("Enter gravitational acceleration: "))
    height = float(input("Enter height in metres: "))
    return mass * gravity * height


print("1. Speed =", speed())
print("2. Force =", force())
print("3. Weight =", weight())
print("4. Kinetic Energy =", kinetic_energy())
print("5. Potential Energy =", potential_energy())
