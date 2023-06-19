from collections import Counter
from sys import stdin

rd = stdin.readline

def psychological_distance(mbti1, mbti2):
    return sum([n != m for n, m in zip(mbti1, mbti2)])

for t in range(int(input())):
    N = int(rd().rstrip())
    MBTI = list(rd().rstrip().split())
    if max(Counter(MBTI).values()) >= 3:
        print(0)
    else:
        distances = []
        for i in range(len(MBTI) - 2):
            for j in range(i + 1, len(MBTI) - 1):
                for k in range(j + 1, len(MBTI)):
                    distances.append(psychological_distance(MBTI[i], MBTI[j]) + psychological_distance(MBTI[j], MBTI[k]) + psychological_distance(MBTI[k], MBTI[i]))
        print(min(distances))