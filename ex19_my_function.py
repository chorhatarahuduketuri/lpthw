def my_function(my_variable):
    print "My variable is: %r" % my_variable

prompt = '-->'

print "One:"
my_function(1)

print "Two:"
my_function('1')

print "Three:"
uno = 1
my_function(uno)

print "Four:"
print "Please enter my_variable here:"
my_function(raw_input(prompt))

print "Five:"
my_function(1+3)

print "Six:"
print "Please input something:"
my_function(('1' + raw_input(prompt)))

print "Seven:"
print "Please input something else:"
something_else = raw_input(prompt)
my_function(something_else)

print "Eight:"
formatter = "%r %r %r %r"
my_function(formatter % (raw_input(prompt),raw_input(prompt),raw_input(prompt),raw_input(prompt)))

print "Nine:"
my_function('placeholder')

print "Ten:"
my_function('placeholder')