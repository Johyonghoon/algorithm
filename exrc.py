import sys

input_data = sys.stdin.readline().strip()
input_data = input_data.replace("[", "").replace("]", ""). replace(" ", "")
ls = list(map(int, input_data.split(",")))
print(ls)