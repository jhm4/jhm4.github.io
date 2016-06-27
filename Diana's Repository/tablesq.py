import sqlite3

info = []

info.append('Diana')
info.append(17)
info.append('Alligator')
info.append(1.34)
info.append('Allie')

info2 = []

info2.append('Lola')
info2.append(5)
info2.append('Tiger')
info2.append(4)
info2.append('Talia')

#establish a connection object to database 
conn = sqlite3.connect('diana.db')


#build a cursor object and call its execute() method to perform SQL commands
c = conn.cursor()
c.execute('''CREATE TABLE stocks7 (Name text, Age integer, Fav_animal text, gpa real, best_friend text, la text, lu text)''')


#Insert row of data 
#c.execute("INSERT INTO stocks VALUES (info[0], info[1], info[2], info[3], info[4])")

animal = 'Panda'
name = 'Talia'

c.execute("INSERT INTO stocks7 VALUES (?,  ?, ?, ?, ?, NULL, NULL )", info)
c.execute("INSERT INTO stocks7 VALUES (?, ?, ?, ?, ?, NULL, NULL)", info2)
c.execute("UPDATE stocks7 SET Fav_animal = ? WHERE best_friend = ?", (animal, name))

#save (commit) the changes 
conn.commit()

conn.close()
