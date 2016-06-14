x = 4
if x == 2:
    print ("x equals two!")
elif x == 3:
    print ("x equals three.")
else:
	print("x does not equal two or three")

print("----------------------------------------")

x = [1,2,3]
y = x
print (x == y) # Prints out True
print (x is y) # Prints out False


print("----------------------------------------")


# change this code
number = 16
second_number = 0
first_array = [1, 2, 3]
second_array = [1,2]

if number > 15:
    print ("1")

if first_array:
    print ("2")

if len(second_array) == 2:
    print ("3")

if len(first_array) + len(second_array) == 5:
    print ("4")

if first_array and first_array[0] == 1:
    print ("5")

if not second_number:
    print ("6")