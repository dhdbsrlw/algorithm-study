import sys

input = sys.stdin.readline

channel = int(input())
b_num = int(input())
b_list = list(map(int, input().split()))

# Initialize (only + / -)
cnt = abs(channel - 100)

# Update
for num in range(1000001):
    str_num = str(num)
    for i in range(len(str_num)):
        if int(str_num[i]) in b_list:
            break
        # last
        elif i == len(str_num) - 1:
            cnt = min(cnt, abs(channel - num) + len(str_num))

print(cnt)
