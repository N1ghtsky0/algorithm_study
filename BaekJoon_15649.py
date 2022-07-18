# BaekJoon 15649
# https://www.acmicpc.net/problem/15649

#dfs
N, M = map(int, input().split())
arr = list(range(1, N + 1))
 
def solution(n, arr, R):
    # 마지막 층에 도착했을 경우 2중 리스트에서 값을 꺼내고 출력
    if n == 1:
        print(' '.join([str(i) for i in R[0]]))
    else:
        # 시작값에서 끝값까지 하나씩 끝까지 찾아가서 출력 후 다음 값으로 넘어감
        for r in R:
            for i in arr:
                # copy를 안할 경우 원본이 변경되어 출력이 이상해짐
                tmp = r.copy()
                if i not in tmp: 
                    tmp.append(i)
                    # 재귀 호출할 때 tmp를 감싸 주지않으면 정수데이터가 넘어가져서 오류 발생
                    solution(n - 1, arr, [tmp])
if M == 1:
    for i in arr: print(i)
else: solution(M, arr, [[i] for i in arr])
