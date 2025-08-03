def floyds_traingle(n):
    c = 1
    for i in range(1, n + 1):          # loop over rows
        for j in range(1, n + 1):      # loop over columns (up to n, but with condition)
            if j <= i:                 # ensures triangle shape
                print(f"{c:<2}", end=" ")
                c += 1
        print()                        # new line after each row

floyds_traingle(5)
