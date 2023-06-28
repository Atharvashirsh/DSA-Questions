lock = "210"
key = list(lock)
key.sort()
# print(key)

if key[0] == "0":
    # print("here")
    count = 0
    while key[count] == "0":
        count += 1
    # print(count)
    key[0], key[count] = key[count], key[0]
    # key = list(key[count]) + key[0:count] + key[count + 1 :]
key = "".join(key)
print(key)
