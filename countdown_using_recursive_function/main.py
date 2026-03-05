num = 5

def count_down(n):
    if n == 0:
        return "Blast Off!"

    print(n)
    return count_down(n - 1)


print(count_down(num))