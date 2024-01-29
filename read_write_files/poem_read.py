<<<<<<< HEAD
=======
"""
poem.txt contains famous poem "Road not taken" by poet Robert Frost. You have to read this
 file in your python program and find out words with maximum occurance.
"""
>>>>>>> a8cee10eed3c645c7c9430480f70fa6214cb7297
import time

word_count = {}
with open("poem.txt","r") as poem:
    for line in poem:
        line.replace("\n","")
        words = line.split(" ")
        for word in words:
            if word in word_count:
                word_count[word] +=1
            else:
                word_count[word] = 1
    poem.close()

word_occurances = list(word_count.values())
max_count = max(word_occurances)
print(max_count)