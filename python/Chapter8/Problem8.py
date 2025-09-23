def table(n, count = 1):
    if count == 10:
        return count
    else:
        print(n, "x", count , "=", n * count)
        return table(n, count = count + 1)

table(5)