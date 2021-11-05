n = int(input())
t = list(map(int, input().rstrip().split()))
x = set(t)
command = int(input())
i = 0
for _ in range(command):
    while i < command:
        z = input().split()
        if z[0] == 'pop':
            x.pop()
            i = i + 1
            break
        elif z[0] == 'discard':
            v = int(z[1])
            x.discard(v)
            i = i + 1
            break
        elif z[0] == 'remove':
            v = int(z[1])
            x.remove(v)
            i = i + 1
            break
o = 0
for n in x:
    o = o + n
print(o)












