def func_name():
    from time import sleep
    from quitting import eq

    all = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '']
    name = '200'

    while True:
        n = input('What is the name? ')
        sleep(1)

        for index, var in enumerate(n):
            if n[index] in all:
                print('Please enter a valid name.')
                sleep(1)
                eq()
                break
        else:
            name = n
        if name == '200':
            continue

        return name
