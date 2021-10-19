# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

# Part 1: Greet Template
def greet(name: str, greeting: str = "Hello, <name>!"):
    return greeting.replace("<name>", name)


print(greet('Doc'))
print(greet('Bob', "What's up, <name>!"))



# Part 2: Force
# https: // www.mathsisfun.com/physics/gravity.html
# https: // www.smartconversion.com/otherInfo/gravity_of_planets_and_the_sun.aspx

def force (mass=0.1, body='earth'):
    gravity_planets={
       "sun": 274,
       "jupiter": 24.2,
       "neptune": 11.2,
       "saturn": 10.4,
       "earth": 9.8,
       "uranus": 8.9,
       "venus": 8.9,
       "mars": 3.7,
       "mercury": 3.7,
       "moon": 1.6,
       "pluto": 0.6
    }
    return mass * gravity_planets[body]


# Part 3: Gravity
# https: // www.mathsisfun.com/physics/gravity.html
# pull = G × ((m1 × m2)/d2)

def pull(m1="float", m2="float", d="float"):
    G = 6.674 * 10 ** -11
    pull = G * ( (m1*m2)/ d ** 2)
    return pull













