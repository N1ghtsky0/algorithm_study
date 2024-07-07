fb_strings = [input() for _ in range(3)]
for i, fb_string in enumerate(fb_strings):
    if fb_string.isdigit():
        fb_target = int(fb_string) + (3 - i)
        if fb_target % 3 == 0 and fb_target % 5 == 0: print("FizzBuzz")
        elif fb_target % 3 == 0: print("Fizz")
        elif fb_target % 5 == 0: print("Buzz")
        else: print(fb_target)
        break