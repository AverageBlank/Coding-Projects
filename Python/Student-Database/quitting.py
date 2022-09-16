def eq():
    from time import sleep
    while True:
        temp = input('Do you want to quit(yes or no)? ').lower()
        if temp != 'yes' and temp != 'no':
            sleep(1)
            continue
        elif temp == 'yes':
            sleep(1)
            quit()
        elif temp == 'no':
            sleep(1)
            break