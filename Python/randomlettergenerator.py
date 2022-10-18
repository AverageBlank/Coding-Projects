from random import choice, randint

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
output = []

for i in range(26):
    temp = choice(list)
    while True:
        if temp in output:
            temp = choice(list)
        else:
            break
    output += temp

print(output)
print(len(output))

list = [str(x) for x in range(0,10)]
output = []

for i in range(10):
    temp = choice(list)
    while True:
        if temp in output:
            temp = choice(list)
            continue
        else:
            break
    output.append(temp)

print(output)
print(len(output))
