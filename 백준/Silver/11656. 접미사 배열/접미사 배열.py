import sys
string = input()

length = len(string)
a = []

for i in range(length):
  a.append(string[-i:])

a.sort()
for i in range(length):
  print(a[i])