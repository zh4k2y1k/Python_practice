from itertools import permutations

a = permutations(input())

for perm in list(a):
    print(''.join(perm))

