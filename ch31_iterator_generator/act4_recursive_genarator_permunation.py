# def permutations(items):
#     n = len(items)
#     if n == 0:
#         yield []
#     else:
#         for i in range(len(items)):
#             for cc in permutations(items[:i] + items[i + 1:]):
#                 yield [items[i]] + cc

# for p in permutations(['r', 'e', 'd']):
#     print(''.join(p))
# for p in permutations(list("game")):
#     print(''.join(p) + ", ", end="")

# print()

# import itertools
# perms = itertools.permutations(['r','e','d'])
# print(type(perms))
# print(list(perms))


def k_permutations(items, n):
    if n == 0:
        yield []
    else:
        for i in range(len(items)):
            for ss in k_permutations(items, n - 1):
                if items[i] not in ss:
                    yield [items[i]] + ss

for p in k_permutations(['r', 'e', 'd', 's'], 3):
    print(''.join(p))
