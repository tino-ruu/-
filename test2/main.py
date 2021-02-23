import re

l = "Beautiful is better than ugly."
matches = re.findall("Beatiful", l)

print(matches)

import re

line = "123 hi 34 hello"
m = re.findall("\d, line, re.IGNORECASE")
print(m)