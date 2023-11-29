#!/usr/bin/python3
for i in range(85, 142):
    if (i == 103) or (i == 117):
        continue
    print(chr(i).format(), end="")
