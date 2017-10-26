n = int(input())
s = []
for i in range(n):
    s.append(input())

for _str in s:
    even = ''
    odd = ''
    for id, _char in enumerate(_str):
        if id % 2 == 0:
            even += _char
        else:
            odd += _char
            
    print(even, odd)