import re

text = """my phone number is +91-9897976962 and my company name is a1technology i have a growt rate of 1000billion dollars
and my usa number is (999)-450-9876"""
pattern = "\(\d{3}\)-\d{3}-\d{4}|\d{10}|\d{2}-\d{10}"

matches = re.findall(pattern, text)
print(matches)