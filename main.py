def main():
    mass = float(input('Enter mass in kilograms: '))
    velocity = float(input('Enter velocity in meters per second: '))
    kinetic_energy(mass, velocity)

def kinetic_energy(mass, velocity):
    oke = 0.5 * mass * velocity ** 2
    print("The object's kinetic energy is ", format(oke, '.2f'), ' J.', sep='')

main()