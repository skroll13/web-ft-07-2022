#dictionaries

#dictionary = {}

#dictionaryName = {key : value}

contacts = {
    "firstName" : "Shannon",
    "phone" : "333-333-3333",
    "city" : "Phoenix",
    "zip" : "77201",
    "isFriendly": True,
    "myList" : [0, 1, 2]
}
# result = contacts["isFriendly"] #this is how to reference the dictionary
# print(result)
#can have a list as a value, not a key
#can have a function as a value, not a key

result = "state" in contacts #is this string in my dictionary? will return True or False. in this case, False
print(result)

contacts["state"] = "Arizona" #this is how you add another key:value. this is also how you change a key:value