max_len = 0
str_arr = []
for _ in range(5):
    s = input()
    max_len = max(max_len, len(s))
    str_arr.append(s)

result = ""
for i in range(max_len):
    for s in str_arr:
        if len(s) > i: result += s[i]
print(result)