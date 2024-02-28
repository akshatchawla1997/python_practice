"""
 Companies in europe reports their financial numbers of semi annual basis and you can have
 a document like this. To exatract quarterly and semin annual period you can use a regex 
 as shown below
"""


import re
text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''

pattern = 'FY\d{4} [A-Z]\d'
matches = re.findall(pattern, text)
print(matches)