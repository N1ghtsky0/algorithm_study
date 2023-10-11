from itertools import permutations
N = int(input())
print('\n'.join([' '.join(map(str, p)) for p in permutations(range(1, N+1), N)]))