print("Question 1")

print('Hello My name is "Rishabh". I love Coding')
print("This is 'my first program'")

x = int(input("x="))
y = int(input("y="))
z = int(input("z="))

print("Output: Value1=%d Value2=%d Value3=%d" % (x,y,z))
print(type(x), type(y), type(z))

print("\nQuestion 2")

print("Hello! My name is XYX")
print("Hello I am a candidate")
print("234.56")
print("34")
print("a+3j")

print("\nQuestion 3")

x = 10+20*(45+67.0)
print(type(x))
x = (True and False) or False
print(type(x))
x = (True or True) and (not False and True)
print(type(x))
x = (3>89) or (34>32)
print(type(x))
x = not True and False
print(type(x))

print("\nQuestion 4")

inp = int(input("Enter a number: "))
if (inp % 2 == 0) and (inp % 5 == 0):
    print("Hurray it is what I am looking for")
else:
    print("Wrong Input")

print("\nQuestion 5")
inp = int(input("Enter a number: "))
if (inp >=10) and (inp <=50):
    print("Yes I am in the range")
else:
    print("Oops")
