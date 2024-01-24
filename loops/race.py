"""Lets say you are running a 5 km race. Write a program that,

Upon completing each 1 km asks you "are you tired?"
1.If you reply "yes" then it should break and print "you didn't finish the race"
2.If you reply "no" then it should continue and ask "are you tired" on every km
3.If you finish all 5 km then it should print congratulations message"""

for i in range(5):
    print(f"you ran {i+1} km")
    tired = input("enter yes or no :")
    if tired == "yes":
        break

if i == 4:
    print("Congratulations you completed the race")
else:
    print("you didn't completed the race and you can't take rest")