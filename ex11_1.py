print "What is your favourite army in 40k?"
favourite_army = raw_input()

print "What is your reason for this?"
reason = raw_input()

print "Your favourite army is %s, and they are your favourite because %s." % (favourite_army, reason)

print "\nHere's an input with a custom prompt: "
after_prompt = raw_input("--->")
print "This is what you input:", after_prompt