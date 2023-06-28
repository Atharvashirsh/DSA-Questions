num = int(input())
num_str = str(bin(num)).replace("0b", "").replace("1", "2")
print(num_str)
