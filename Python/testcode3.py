# This prints out "John is 23 years old."
name = "John"
age = 23
print ("%s is %d years old." % (name, age))

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print ("A list: %s" % mylist)

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is %.2f$"

print (format_string % data)

print("--------------------------------------")

astring = "Hello world!"

print(astring.split(" "))

print("--------------------------------------")

s = "Strings are awesome!"
# Length should be 20
print ("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print ("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print ("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print ("The first five characters are '%s'" % s[:5]) # Start to 5
print ("The next five characters are '%s'" % s[5:10]) # 5 to 10
print ("The twelfth character is '%s'" % s[12]) # Just number 12
print ("The characters with odd index are '%s' " %s[1::2]) #(0-based indexing)
print ("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print ("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print ("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print ("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print ("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print ("Split the words of the string: %s" % s.split(" "))