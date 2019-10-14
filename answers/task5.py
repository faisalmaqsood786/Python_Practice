import re

input = "45 >= 67 25==70 30 <= 78"
text = re.findall('(\d+\s?(<|=|>)=\s?\d+)', input)
output = ""
for i in text:
    if eval(i[0]):
        output += "1"
    else:
        output += "0"
print(output)
