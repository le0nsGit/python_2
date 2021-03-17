

#define some functions
def function0():
  print("This is function 0")

def function1():
  print("This is function 1")

def function2():
  print("This is function 2","\n")


## Append the functions to a list
list_of_functions = (function0, function1, function2)

## Call each of the functions one at a time
print("\nHow to call each function in a list of functions.")
list_of_functions[0]()
list_of_functions[1]()
list_of_functions[2]()


## Loop over the entire list of functions call each in order
print("\nHow to iterate through a list of functions.\n")
for i in range(len(list_of_functions)):
  list_of_functions[i]()



## define some functions with parameters
def function3(x):
  print("This is function ", x,"\n")


def function4(x,y):
  print("This is function ", x)
  print("I have $", y,"\n")

def function5(x,y,z):
  print("This is function ",x)
  print("The sun is yellow: ", y)
  print(f'I am {z} in line.\n')

# list of functions with parameters


## Append the functions to a list
list_of_functions2 = [ function3, function4, function5 ]

## Call each of the functions one at a time
print("\nHow to call each function in a list of functions.")
list_of_functions2[0](3)
list_of_functions2[1](4, "340.00")
list_of_functions2[2](5, True, "First")


## Loop over the entire list of functions call each in order
print("\nHow to iterate through a list of functions.\n")
for i in range(len(list_of_functions2)):
  list_of_functions[i]()


## define some functions with *args and **kwargs
def function3(x):
  print("This is function ", x)

def function4(x,y):
  print("This is function ",x)
  print("The don't have $ ", y,"\n")


def function5(*args):

    print(args,"\n")

    print("This is function ",args[0])
    print("The see is blue: ", args[1])
    print(f'I am {args[2]} in line, again.\n')

def function6(**kwargs):

    print(kwargs)

    print("This is function ",kwargs["x"])

    print("I have $", kwargs.get("y"))


# Append the functions to a list
list_of_functions2 = [ function3, function4, function5, function6 ]

# Call each of the functions one at a time
print("\nHow to call each function in a list of functions.")
list_of_functions2[0](3)
list_of_functions2[1](4, "340.00")
list_of_functions2[2](5, True, "First")
list_of_functions2[3](x=5,y=600.00)



# Append the functions to a dictionary
dict_of_functions = {0: function3, 2: function4, "Steve": function5, 26.00: function6}

# Call each of the functions one at a time
print("\nHow to call each function in a list of functions.")
dict_of_functions.get(0)(3)
dict_of_functions.get(2)(4,750.00)
dict_of_functions.get("Steve")(5,False, "I'm broke")
dict_of_functions.get(26.00)(x=6)



