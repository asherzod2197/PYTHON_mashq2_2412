for son in range(2, 101):
    tub = True
    for i in range(2, son):
        if son % i == 0:
            tub = False
            break

    if tub:
        print(son)
