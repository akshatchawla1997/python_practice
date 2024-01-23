"""Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
i.    Ask user to enter his fasting sugar level
ii.   If it is below 80 to 100 range then print that sugar is low
iii.  If it is above 100 then print that it is high otherwise print that it is normal
"""

sugar=input("Please enter your fasting sugar level:")
sugar=float(sugar)
if sugar<80:
    print("Your sugar is low, go eat some jalebi :)")
elif sugar>100:
    print("Your sugar is high, stop eating all mithais..!")
else:
    print("Your sugar is normal, relax and enjoy your life!")