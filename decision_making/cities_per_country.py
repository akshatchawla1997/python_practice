"""Using following list of cities per country,
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
i).  Write a program that asks user to enter a city name and it should tell which country 
     the city belongs to
ii). Write a program that asks user to enter two cities and it tells you if they both are
     in same country or not. For example if I enter mumbai and chennai, it will print "Both
     cities are in India" but if I enter mumbai and dhaka it should print "They don't
     belong to same country"""

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
city = input("enter a city name to find the country : ")

# i).  Write a program that asks user to enter a city name and it should tell which country 
#      the city belongs to
if city in india:
    print(f"{city} found in INDIA")
elif city in pakistan:
    print(f"{city} found in PAKISTAN")
elif city in bangladesh:
    print(f"{city} found in BANGLADESH")
else:
    print("No Country found of this city")


"""
    ii). Write a program that asks user to enter two cities and it tells you if they both are
     in same country or not. For example if I enter mumbai and chennai, it will print "Both
     cities are in India" but if I enter mumbai and dhaka it should print "They don't
     belong to same country
"""

city2 = input("Enter second city : ")

if city in india and city2 in india:
    print(f"Both cities belong to INDIA")
elif city in pakistan:
    print(f"Both cities belong to PAKISTAN")
elif city in bangladesh:
    print(f"Both cities belong to BANGLADESH")
else:
    print("they both belong to different Countries")