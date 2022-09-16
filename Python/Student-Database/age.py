def func_age(d):
    all = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z' '-', '.', '-', '=', '+', '_', '[', ']', '{', ' ', '}', '|', '\\', ';', "'", '"', ':', ';', '/', '.', ',', '>', '<', '?', '']
    from time import sleep
    from quitting import eq
    while True:
        a = input(f"What is {d}'s age? ")
        sleep(1)
        age = '200'
        for index, var in enumerate(a):
            if a[index] in all:
                print('Please enter the correct age.')
                sleep(1)
                eq()
                break
        else:
            age = int(a)
        if age == '200':
            continue
        if age > 20 or age < 6:
            print('Please enter the correct age.')
            sleep(1)
            eq()
            continue

        return age
