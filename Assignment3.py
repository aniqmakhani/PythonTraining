# Question No: 01 Write a Solution to reverse every alternate k characters from a
# string. Ex. k = 2 , Input_str ="abcdefg", Output_str = bacdfeg"

print("Question 1: ")
Input_str = input("Enter a string: ")
k = int(input("Enter a value for k: "))
inp = list(Input_str)
for i in range(0,len(inp),k+2):
    if i+1 < len(inp):
        inp[i], inp[i+1] = inp[i+1], inp[i]
inp = "".join(inp)
print(inp)


#-----------------------------------------------------------

# Question No: 02 Write a Solution to replace unwanted charecters("CON") from the
# String. Ex. Input_str = "PCONECONCONN", Output_str = "P E N"

print("\nQuestion 2: ")

Input_str = "PCONECONCONN"
print(Input_str)
print(Input_str.replace("CON", ''))


#-------------------------------------------------------------

# Question No: 03 Write a solution to replace the Character value with its
# corresponding value from the String. Replace 'A' with 'T', 'T' with 'A' and 'C' with 'G',
# ''G' with 'C'. Input_str ="ATTCGGTAG", Output_str = "TAAGCCATC"
print("\nQuestion 3: ")
str_dict = { 'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C' }
x = input("Enter a string: ")
new_str = []
for str in x:
    new_str.append(str_dict.get(str, ''))
final_str = "".join(new_str)
print(final_str)

#----------------------------------------------------------------
# Question No: 04 Write a Solution to fetch out the serial number from the given
# Reciept Input of Product. The serial number will be fetched by combining all the
# values of date printed over the Receipt. Input_str = "2012-18-10 Speaker Harman",
# Output_str = "20121810"

import re

print("\nQuestion 4: ")

inp_str = "2012-18-10 Speaker Harman"
num = re.findall("\d+", inp_str)
num = "".join(num)
print(num)
