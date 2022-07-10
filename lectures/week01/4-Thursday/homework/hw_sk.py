# Homework
## Iterative Programming

#### 1. Multiply Vectors

# Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists. Example:

# ```
# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]
# ```

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# results_list=[]
# for i in range(0, len(list1)):
#     results_list.append(list1[i] * list2[i])
# print(results_list)

#### 2. Matrix Addition

# Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists:

# ```
# [ [2, -2],
#    [5, 3] ]
# ```

# Calculate the result of adding the two matrices. The number in each position in the resulting matrix should be the sum of the numbers in the corresponding addend matrices. Example: to add

# ```
# 1 3
# 2 4
# ```
# and

# ```
# 5 2
# 1 0
# ```

# results in

# ```
# 6 5
# 3 4
# ```

# a=[[1, 2, 3, 4], [5, 1, 2, 0]]


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# results_list=[]
# for i in range(0, len(list1)):
#     results_list.append(list1[i] + list2[i])
# print(results_list)



# #### 3. Matrix Addition II

# Use your solution in Matrix Addition, and extend it to work for a pair of matrices of any size, as long as they have the same size.

# list1 = [1, 2, 3, 3, 3, 4]
# list2 = [4, 5, 6, 6, 6, 7]
# results_list=[]
# for i in range(0, len(list1)):
#     results_list.append(list1[i] * list2[i])
# print(results_list)

# #### 4. De-dup

# Given a list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. Print the list.

# first_list = [1, 2, 3, 4, 1, 2, 3, 4, 5, 5, 5,]
# print("The first list is: " + str(first_list))

# no_dups = []
# for i in first_list:
#     if i not in no_dups:
#         no_dups.append(i)
# print("We don't want no Dups. Dups are a number that can't get no love from me: " + str(no_dups))            

# #### 5. Leetspeak

# Given a paragraph of text as a String, print the paragraph in [leetspeak](https://en.wikipedia.org/wiki/Leet). 

# To translate a String to leetspeak, you need to replace make the following character replacements (treat all input characters as uppercase):

# | Letter | Translates To |
# |:------:|:-------------:|
# | A      | 4             |
# | E      | 3             |
# | G      | 6             |
# | I      | 1             |
# | O      | 0             |
# | S      | 5             |
# | T      | 7             |

# Example: If your program is given the String `"I am a leet programmer"`, it should print `"1 4m 4 l337 pr0gr4mm3r"` as the leetspeak translation

# fun_fact = "I am a leet programmer"

# cipher = {'A':'4',
#         'E':'3',
#         'G':'6',
#         'I':'1',
#         'O':'0',
#         'S':'5',
#         'T':'7'}

# wild_times = ' '

# for letter in fun_fact:
#     if letter.upper() in cipher.keys():
#         wild_times += cipher[letter.upper()]
#     else:
#         wild_times += letter
# print(wild_times)

# #### 6. Long-long Vowels

# Given a word as a string, print the result of extending any long vowels to the length of 5. 
##### THIS STILL NEEDS WORK

# starting_string = "pray! maid raids!"

# def isVowel (ch):
#     ch = ch.lower()
#     if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch =='u'):
#         return True
#     else:
#         return False

# def duplicateVowels (starting_string):
#     t = len(starting_string)
    
#     result = ""
    
#     for i in range(t):
#         if (isVowel(starting_string[i])):
#             result += starting_string[i]
#         result += starting_string[i]
#     return result
# print(starting_string)

# result = duplicateVowels(starting_string)

# print("long vowel party: ", result)

##### credit: https://www.geeksforgeeks.org/program-to-duplicate-vowels-in-string/

# Examples:

# ```
# Good => Goooood 
# Cheese => Cheeeeese 
# Man => Man 
# Spoon => Spooooon 
# ```

# #### 7. Caesar Cipher

# Given a string, print the Caesar Cipher (or ROT13) of that string. What is Caesar Cipher? [Learn about it here](http://practicalcryptography.com/ciphers/caesar-cipher/).

# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"

# def decrypt(key, message):
#     message = message.lower()
#     alpha = "abcdefghijklmnopqrstuvwxyz"
#     result = ""
        
#     for letter in message:
#         if letter in alpha: #if the letter is actually a letter
#             #find the corresponding ciphertext letter in the alphabet
#             letter_index = (alpha.find(letter) - key) % len(alpha)

#             result = result + alpha[letter_index]
            
#     return result

# def main():
#     code_words = "lbh zhfg hayrnea jung lbh unir yrnearq"
    
#     decrypted = decrypt(13,code_words)
#     print(decrypted)
    
# if __name__ == "__main__":
#         main()
    
##### credit: https://teachen.info/cspp/unit4/lab04-02.html


# ## Large 

# ### Matrix Multiplication
# Given two two-dimensional lists of numbers of the size 2x2 - calculate the result of multiplying the two matrices. Print the resulting matrix.

# list1 = [1, 2]
# list2 = [4, 5]
# results_list=[]
# for i in range(0, len(list1)):
#     results_list.append(list1[i] * list2[i])
# print(results_list)

# How do you multiple two matrices?

