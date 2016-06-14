def function(username, greeting):
    print ("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

function("Bill", "a lousy life")

print("----------------------------------------")


def sum_these(a, b):
    return a + b


print(sum_these(2, 3))


print("----------------------------------------")


# Modify this function to return a list of strings as defined above
def list_benefits():
    array = ["More organized code", "More readable code", "Easier code reuse", 
    "Allowing programmers to share and connect code together"]
    return array

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return benefit + " is a benefit of functions!"

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()

