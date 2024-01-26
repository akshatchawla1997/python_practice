"""
poem.txt contains famous poem "Road not taken" by poet Robert Frost. You have to read this
 file in your python program and find out words with maximum occurance.
"""

with open("poem.txt","r") as poem:
    for line in poem:
        print(line)