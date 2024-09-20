def pattern(n):
    if n == 6:
        return
    print("*" * n)
    pattern(n + 1)

pattern(1)