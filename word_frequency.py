#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)
# 1. Prompt the user: Ask the user to enter a sentence.
# 2. Split the sentence
# 3. Create lists to store words and their corresponding frequencies.
# 4. Iterate through words and update frequencies


    
sentence = input("Enter a sentence: ")# get the user input from the user

sentence_list = sentence.split() # created a new variable called sentse list and then split the sentence

words = []    # using it store each unique word
counts = []   #will store how many times each word appears.

for w in sentence_list: #This starts a loop that goes through each word w in the list sentence_list.
    w = w.strip(".,!?").lower()  # removes punctuation marks from the start or end of the word. and lower makes it lower case
    if w in words: #This checks if the word w is already in the words list.
        index = words.index(w)
        counts[index] += 1
        #If it is already there,  find its positio(index) in the words list.
    else:
        words.append(w)# If the word is not already in the list, we add it to words.
        counts.append(1)

for i in range(len(words)): #This loop goes through all the indexes of the words list.
    print(words[i] + ":", counts[i])
