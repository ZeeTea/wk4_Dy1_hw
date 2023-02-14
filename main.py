# Question1
#Reverse the list below in-place algorithm.
#For extra credit: Reverse the strings at the same time.

def reverse_list(words):
    start = 0
    end = len(words) - 1
    while start < end:
        words[start], words[end] = words[end][::-1], words[start][::-1]
        start += 1
        end -= 1
    return words[::-1]

words = ['this' , 'is', 'a', 'sentence', '.']
print(reverse_list(words))

#Question 2
#Create a function that counts how many distinct words are in the string below, then outputs a dictionary with the words as the key and the value as the amount of times that word appears in the string.
#Should output:
#{'a': 5,
#'abstract': 1,
#'an': 3,
#'array': 2, ... etc...

def word_count(a_text):
    words = a_text.split()
    word_dict = {}
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict

a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'
print(word_count(a_text))

#Question 3
#Write a program to implement a Linear Search Algorithm.
# Hint: Linear Searching will 
# require searching a list for a given number. 
def linear_search(nums_list, target):
    for i in range(len(nums_list)):
        if nums_list[i] == target:
            return i
    return -1

nums_list = [10,23,45,70,11,15]
target = 70
result = linear_search(nums_list, target)

if result != -1:
    print("Target is present at index", result)
else:
    print("Target is not present in the list")
