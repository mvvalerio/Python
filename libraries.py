# import json
# 
# x = {
#     "name": "John",
#     "age": 30,
#     "city": "New York"
# }
# 
# y = json.dumps(x)
# 
# print(y)

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x)