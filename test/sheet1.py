
# print(ord('a'), ord('z')) # 97, 122
l = map(input().lower().count,map(chr,range(97,123)))
m = max(l)
k = [x for x in l if x == m]

if len([x for x in l if x == m]) > 1:
    print('?')
else:
    print(m)


"""
# 2675
T = int(input())
for i in range(T):
    n, s = input().split(" ")
    n = int(n)
    s2 = [x * n for x in s]
    print("".join(s2))
"""

"""
a = [-1] * (ord('z') + 1)
s = input()
for i in range(len(s)):
    if a[ord(s[i])] == -1:
        a[ord(s[i])] = i

s = map(str, a[ord('a'):ord('z') + 1])
print(" ".join(s))
"""