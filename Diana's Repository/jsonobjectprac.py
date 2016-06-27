import json

phonebook = { "Alice" : 905, "Jack" : 345, "Bob" : 587 } 

string = json.dumps(phonebook)

phonebook2 = json.loads(string)
print(phonebook2 == phonebook)