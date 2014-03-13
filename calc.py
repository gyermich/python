def prompt():
  response = raw_input("What would you like to do: add(+), subtract(-), divide(/), myltiply(*) or find a square root(sqrt)?").strip()
  print response
  if response in ["sqrt", 'find square root']:
    c = int(raw_input("Enter a number:"))
  else:
    a = int(raw_input("First Number:"))
    b = int(raw_input("Second Number:"))

  if response == "+":
    result = add(a,b)
  elif response ==  "-":
    result = subtract(a,b)
  elif response ==  "*":
    result = multiply(a,b)
  elif response ==  "/":
    result = divide(a,b)
  elif response ==  "sqrt":
    result = sqrt(c)
  else:
    print "Invalid input"

  print result


def add(a,b):
  return a + b

def subtract(a,b):
  return  a - b

def multiply(a,b):
  return a * b

def divide(a,b):
  return a / b

def sqrt(a):
  return  math.sqrt(a)

prompt()