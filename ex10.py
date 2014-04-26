tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip \n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

tripple_single_quote = '''
what?
'''

print tripple_single_quote

template = 'What happens if you don\'t insert a variable: %r'
print template
template_2 = "What happens if you do: %r" % 5
print template_2,
print "actually, that was a primitive. "

print "an escaped format thing: \%r" % 6,
print "apparently you can't escape the formatting thing. " 

print "escaped percent-r: \%r" 
print "escaped percent-s: \%s"

print "escaped percent-r with variable: \%r" % "what"
print "escaped percent-s with variable: \%s" % "hello"
