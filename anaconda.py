file = """a = 2
b = 3
print add:1,2
print add:a,b
a = 5
b = 8
print add:a,b
a = add:a, 1
print a
print 6"""
input = file.split( '\n')
environment = {}

def addition(line):
  if line.find("add:") != -1:
    tokens = line.split(":")[1].split(",")
    if tokens[0] in environment:
      first_argument = environment[tokens[0]]
    else:
      first_argument = tokens[0]

    if tokens[1] in environment:
      second_argument = environment[tokens[1]]
    else:
      second_argument = tokens[1]

    return int(first_argument) + int(second_argument)


for line in input:
    if line.find("=") != -1:
      tokens = line.split("=")
      tokens = [x.strip() for x in tokens]

      if ":" in tokens[1]:
        environment[tokens[0]] = addition(tokens[1])
      else:
        environment[tokens[0]] = tokens[1]
    elif "print" in line:
      tokens = line.split( )
      if tokens[1] in environment:
        print environment[tokens[1]]
      elif ":" in tokens[1]:
        print addition(tokens[1])
      else:
        print tokens[1]



















