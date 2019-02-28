import re
vowelregex = re.compile(r'[^aeiouAEIOU]')
m=vowelregex.findall('RoboCop Eats baby FoOd')
print(m)

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-6988')
print('Phone no Found: '+mo.group())

