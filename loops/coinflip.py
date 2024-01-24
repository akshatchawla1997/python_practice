"""
After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
Using for loop figure out how many times you got heads
"""
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count =0
# method 1
for item in result:
    if item == "heads":
        count = count+1

print(f"{count} method 1 ")

# method 2

heads_count = result.count("heads")
print(f"{heads_count} method 2")

# method 3  

heads_count = sum(1 for flip in result if flip == "heads")

print(f"{heads_count} by method 3")