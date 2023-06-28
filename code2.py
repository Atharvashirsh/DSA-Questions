"""
Find occurences of all characters in a string
"""


char = "atharva"
name = "".join(set(char))
# print(name) # Unique name characters

for key in name:
    print(f"{key}  {char.count(key)}")
