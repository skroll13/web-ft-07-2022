# Return a new list with each element multiplied by 5

from turtle import position
from unicodedata import name

nums = [56, 34, 34, 1, 1, 1, 23, 12, 89, 89, 89, 70, 56] 
# initialize a new empty list -- this is where I'm going to put the new multiplied values into
# for each in my list of nums
#    multiply the current number by 5
#    append to the end of the new list
newList = []
for curItem in nums:
    #temp = curItem * 5
    #newList.append(temp)
    newList.append(curItem * 5)

# while look -- what do I need do and how do I know when to stop?
# initialize a new list, empty
# how many items are in the list -- this is going to tell me how many times to repeat

# I need to take each item from the list, one at time, and multiply it by five and then put the new value into my new list
    
nums4 = [56, 34, 34, 1] 
#        [0 ,  1,  2,  3] 
newList = []
itemCount = len(nums4) # how many items are in nums4? 4
positionNumber = 0 # start at first position in my list; var is the index/position of the item I'm looking at in list currently
while (positionNumber < itemCount):
    # grab the value/item from nums4 at postionNumber
    temp = nums4[positionNumber]
    # multiply value by 5
    temp = temp * 5
    # append it to my new list
    newList.append(temp)
    # newList.append(nums4[positionNumber]*5)
    positionNumber += 1
    
# initialize some variable you will change inside of the loop and will check each iteration; e.g. position
posNum = 0
while (posNum < 3):
    print("hi")
    posNum += 1
    
    # posNum = 0 hi
    # posnNum = 1 hi
    # posNum = 2 hi
    # posNum = 3
    

############3

nums1 = [56, 34, 34, 1, 1, 1, 23, 12, 89, 89, 89, 70, 56] 
nums2= [3, 12, 13, 33, 1, 8, 42]
nums3= [17, 2]
newList=[]
for currentNum in nums2:
    print("hi " + currentNum)

    
# currentNum = 3 # first item/number in nums2
# print("hi + " + currentNum) # hi + 3 --> hi 3
# currentNum = 12
# print("hi + " + currentNum) # hi + 12 --> hi 12
# currentNum = 13
# print("hi " + currentNum) # hi 13
# ...




# Given a list [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this {'job': 'Instructor', 'name': 'Elie'} (the order does not matter).
myList=
my_dictionary={}
for in range(len(myList))
