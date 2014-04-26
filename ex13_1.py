from sys import argv

script, first, second, third, fourth = argv

data_one = raw_input("%r is :" % first)
data_two = raw_input("%r is :" % second)
data_three = raw_input("%r is :" % third)
data_four = raw_input("%r is :" % fourth)

print "%r = %r" % (first,data_one)
print "%r = %r" % (second,data_two)
print "%r = %r" % (third,data_three)
print "%r = %r" % (fourth,data_four)