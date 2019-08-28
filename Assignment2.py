print("Question 1:")

x = [1,2,3,4,[10,20,30,40,[100,200,300,400],"rishabh_",5+5j],4000]
print(x[4][:2])
print(x[4][6])
print(x[4][4][2:])
print(x[4][3:6])

#------------------------------------------------------------------------------------------

print("\nQuestion 2:")
for i in range(1,21):
    for j in range(i+1,21):
        if (i+j) % 2 == 0:
            print("Pair (%d,%d) with the sum of %d which is even" % (i, j, i+j))

#------------------------------------------------------------------------------------------
print("\nQuestion 3:")

from collections import Counter

str = input("Please input a string: ")
dict = Counter(str)
dict = {key:value for key, value in dict.items() if not key.isalpha()} # remove all the alphabets
                                                                            #from the dictionary
print(dict)

#------------------------------------------------------------------------------------------

print("\nQuestion 4:")

for i in range(1,51):
    if (i**3) % 2 == 0:
        pass
    else:
        print("Number %d has a cube of %d which is an odd number" % (i,i**3))

#------------------------------------------------------------------------------------------

print("\nQuestion 5:")

items = [1,2,3,4,5,6,7,8,9,10]
copy_items = [item*3 for item in items]
print(copy_items)

#------------------------------------------------------------------------------------------

print("\nQuestion 6:")
sentence = "Hello world I am learning python"
print(sentence)

sen_arr = sentence.split()
for sen in sen_arr:
    print("length of %s is %d" % (sen, len(sen)))

#------------------------------------------------------------------------------------------

print("\nQuestion 7:")

arraylist = [1,2,3,4,5,6,7,8,9]
check = True
for i in arraylist:
    if type(i) == int:
        check = True
    else:
        check = False
        print(check)
        break
if check == True:
    print(check)
