from collections import deque
def solution(order):
    answer = 0
    main_container = deque(range(1, len(order) + 1))
    sub_container = list()
    order_idx = 0
    while True:
        if main_container and main_container[0] == order[order_idx]:
            main_container.popleft()
            answer += 1
            order_idx += 1
        elif sub_container and sub_container[-1] == order[order_idx]:
            sub_container.pop()
            answer += 1
            order_idx += 1
        else:
            if not main_container: break
            sub_container.append(main_container.popleft())
    return answer