import re

text="""chat1 .=. 'codebasics: .you-ask.lot.of-questions ..
.1235678912, -abc@xyz.com'-
chat2 .=. 'codebasics: .here.it.is: .(123)-567-8912,.
abc@xyz.com'a
chat3 .=. 'codebasics :- yes, -phone: - 1235678912-email :.
abc@xyz.com'"""

phone = "\(\d{3}\)-\d{3}-\d{4}|\d{10}"
email = "[a-zA-Z1-9]*@[a-zA-Z]+\.[a-zA-Z]*"
phone_match = re.findall(phone, text)
email_match = re.findall(email, text)
print(phone_match, '\n', email_match)
