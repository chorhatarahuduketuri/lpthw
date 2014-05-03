def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d = %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Let's do some maths with just functions!"

fahrenheit = 100
celsius = 1

print "Fahrenheit: %d, Celsius: %d." % (fahrenheit, celsius)

fahrenheit_to_celsius = divide(multiply(subtract(fahrenheit, 32), 5), 9)
celsius_to_fahrenheit = add(32, divide(multiply(celsius, 9), 5))

print "fahrenheit_to_celsius: %d" % (fahrenheit_to_celsius)
print "celsius_to_fahrenheit: %d" % (celsius_to_fahrenheit)