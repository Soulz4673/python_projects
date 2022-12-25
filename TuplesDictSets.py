#list, turple, dictionary

contacts = {} # The global telephone contact list

running = True
while running:
    command = input('A)dd D)elete L)ook up Q)uit: ')
    if command == 'A' or command == 'a' :
        name = input('Enter new name:')
        print('Enter phone number for', name, end=':')
        number = input()
        contacts[name] = number
    elif command == 'D' or command == 'd':
        name = input('Enter name to delete :')
        del contacts[name]
    elif command == 'L' or command == 'l':
        name = input('Enter name :')
        print(name, contacts[name])
    elif command == 'Q' or command == 'q':
        running = False
    elif command == 'dump': # Secret command
        print(contacts)
    else:
        print(command, 'is not a valid command')

#-------------------------------------------
# Convert Tuples to Dictionary
# Using Dictionary Comprehension
# Note: For conversion of two tuples into a dictionary, we've to have the same length of tuples.
# Otherwise, we can not match all the key-value pairs
# initializing tuples
test_tup1 = ('GFG', 'is', 'best')
test_tup2 = (1, 2, 3)
  
# printing original tuples
print("The original key tuple is : " + str(test_tup1))
print("The original value tuple is : " + str(test_tup2))
  
# Using Dictionary Comprehension
# Convert Tuples to Dictionary
if len(test_tup1) == len(test_tup2):
    res = {test_tup1[i] : test_tup2[i] for i, _ in enumerate(test_tup2)}
  
# printing result 
print("Dictionary constructed from tuples : " + str(res))

#-------------------------------------------
# using setdefault()
# Here we have used the dictionary method setdefault() to convert the first parameter to key and the
# second to the value of the dictionary. setdefault(key, def_value) function searches for a key and
# displays its value and creates a new key with def_value if the key is not present. Using the 
# append function we just added the values to the dictionary.
# Python code to convert into dictionary
def Convert(tup, di):
    di = dict(tup)
    return di
      
# Driver Code 
tups = [("akash", 10), ("gaurav", 12), ("anand", 14), 
    ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print (Convert(tups, dictionary))

#------------------------------------
# Python code to convert into dictionary
list_1=[("Nakul",93), ("Shivansh",45), ("Samved",65),
           ("Yash",88), ("Vidit",70), ("Pradeep",52)]
dict_1=dict()
  
for student,score in list_1:
    dict_1.setdefault(student, []).append(score)
print(dict_1)

#------------------------------------
