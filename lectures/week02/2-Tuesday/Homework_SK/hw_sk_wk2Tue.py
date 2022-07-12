from cgi import print_arguments
from itertools import count
import pickle

#.........................................rb = read binary
try:
    with open('phonebook.pickle', 'rb') as filehandler:
        phonebook = pickle.load(filehandler)
except:
    phonebook = {}

    
    
# You will write a command line program to manage a phone book. When you start the phonebook.py program, it will print out a menu and ask the user to enter a choice:

# If they choose to look up an entry, you will ask them for the person's name, and then look up the person's phone number by the given name and print it to the screen.
# If they choose to set an entry, you will prompt them for the person's name and the person's phone number,
# If they choose to delete an entry, you will prompt them for the person's name and delete the given person's entry.
# If they choose to list all entries, you will go through all entries in the dictionary and print each out to the terminal.
# If they choose to quit, end the program.

### print out menu and ask the user to enter a choice
#### look up an entry: 
#### set an entry:
#### delete an entry:
#### list all entries: 
#### quit and save file
menu = ['look up an entry', 'set up an entry', 'delete an entry', 'list all entries', 'quit and save']

def print_menu():
    count = 1
    print("""
        Electronic Phone Book
        ===================##
        """)
    for every_item in menu:
        print(f'{count}: {every_item}')
        count+=1
    print('what would you like to do? >> 1-5')


def lookup_number():
    print('looking up number.....')
    name = input('what is the name? >> ')
    print(phonebook.get(name))
    
def set_entry():
    print('looking up entry.....')
    name = input('what is the name? >> ')
    number = input('what is the number? >>')
    phonebook[name] = number 
    print('added.')

def delete_entry():
    try:
        name = input('what entry would you like to delete? >> ')
        del phonebook[name]
        print('deleted')
    except:
        print('this is not an option for deletion')
        
def list_all():
    for key in phonebook: 
        print(f"{key}:{phonebook[key]}")

def quit_save():
     #........................................wb = write binary   
    with open('phonebook.pickle', 'wb') as filehandler:
        pickle.dump(phonebook, filehandler)
        print("see you later!")

while True:
    print_menu()
    user_prompt = int(input('>> '))
    if user_prompt == 1:
        lookup_number()
    elif user_prompt == 2:
        set_entry()
    elif user_prompt == 3:
        delete_entry()
    elif user_prompt == 4:
        list_all()
    elif user_prompt == 5:
        quit_save()
        break
        





if user_prompt == 1: #look up phone number by name provided by the user
    lookup_number()



# $ python3 phonebook.py

# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit
# What do you want to do (1-5)? 2

# Name: Melissa
# Phone Number: 584-394-5857
# Entry stored for Melissa.

# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit What do you want to do (1-5)? 2

# Name: Igor
# Phone Number: 857-485-2935
# Entry stored for Igor.

# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit What do you want to do (1-5)? 2

# Name: Jazz
# Phone Number: 334-584-2345
# Entry stored for Jazz.

# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit
# What do you want to do (1-5)? 1

# Name: Melissa
# Found entry for Melissa: 584-394-5857

# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit What do you want to do (1-5)? 3

# Name: Melissa
# Deleted entry for Melissa

# Electronic Phone Book
# =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit What do you want to do (1-5)? 4

# Found entry for Igor: 857-485-2935
# Found entry for Jazz: 334-584-2345

# Electronic Phone Book =====================
# 1. Look up an entry
# 2. Set an entry
# 3. Delete an entry
# 4. List all entries
# 5. Quit What do you want to do (1-5)? 5

# Bye.

