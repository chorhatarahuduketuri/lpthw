from sys import argv

script, filename = argv

test_file = open(filename)

test_file_contents = test_file.read()

print test_file_contents

test_file.close()