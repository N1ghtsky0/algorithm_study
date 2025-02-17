def solution(n, bans):
    answer = ''
    bans.sort(key=lambda x:(len(x), x))
    deleted_count = get_deleted_count(bans, get_spell(n))
    while True:
        new_deleted_count = get_deleted_count(bans, get_spell(n + deleted_count))
        if deleted_count == new_deleted_count: break
        deleted_count = new_deleted_count
    return get_spell(n + deleted_count)

def get_spell(n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    spell = ""
    while n:
        spell = alphabet[n % 26 - 1] + spell
        n = n // 26 - (n % 26 == 0)
    return spell

def get_deleted_count(bans, target):
    left, right = 0, len(bans)
    while left < right:
        mid = (left + right) // 2
        if bans[mid] == target: return mid + 1
        tmp = [bans[mid], target]
        tmp.sort(key=lambda x: (len(x), x))
        if tmp[0] == target: right = mid
        else: left = mid + 1
    return left