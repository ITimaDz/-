def number(n, partial=0):
    if n == 0:
        return partial
    return number(n // 10, partial * 10 + n % 10)

trial = 12321
if number(trial) == trial:
    print("Palindrome!")