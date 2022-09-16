def func_grades(e):
    # Imports
    from time import sleep
    from quitting import eq

    # Important Variable
    all = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
           'Y', 'Z' '-', '.', '-', '=', '+', '_', '[', ']', '{', ' ', '}', '|', '\\', ';', "'", '"', ':', ';', '/', '.', ',', '>', '<', '?', '']
    l2n = 0
    st = 0
    st5 = 0
    l3n = 0

    while True:
        # Taking input for grade. 
        c = int(input(f'Which class is {e} in? '))
        sleep(1)
        # Checking grade.
        if c > 12 or c < 1:
            print('Please type in the correct class.')
            sleep(1)
            eq()
            continue
        else:
            break

    while True:
    
    # Grouping Subjects.
        if c >= 1 and c < 3:
            final = 1
            l2 = input(f'What is {e}\'s second language(Type in "t" for Telugu, "h" for Hindi)? ').lower()
            sleep(1)
            # Checking Language
            if l2 != 'h' and l2 != 't':
                print('Please type in the correct language.')
                sleep(1)
                eq()
                continue

            else:
                if l2 == 'h':
                    l2n = 'Hindi'
                elif l2 == 't':
                    l2n = 'Telugu'
                # Marks
                while True:
                    sub = input(f'How much did {e} get in Maths(out of 100)? ')
                    sleep(1)
                    sub1 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub1 = int(sub)
                    if sub1 == '200':
                        continue
                    if sub1 > 100 or sub1 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in Science(out of 100)? ')
                    sleep(1)
                    sub2 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub2 = int(sub)
                    if sub2 == '200':
                        continue
                    if sub2 > 100 or sub2 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in Social Science(out of 100)? ')
                    sleep(1)
                    sub3 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub3 = int(sub)
                    if sub3 == '200':
                        continue
                    if sub3 > 100 or sub3 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in English(out of 100)? ')
                    sleep(1)
                    sub4 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub4 = int(sub)
                    if sub4 == '200':
                        continue
                    if sub4 > 100 or sub4 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in {l2n}(out of 100)? ')
                    sleep(1)
                    sub5 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub5 = int(sub)
                    if sub5 == '200':
                        continue
                    if sub5 > 100 or sub5 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue
                    break
                break

        elif c >= 3 and c < 5:
            final = 2
            l2 = input(f'What is {e}\'s second language(Type in "t" for Telugu, "h" for Hindi, "f" for French)? ').lower()
            sleep(1)
            # Checking Language
            if l2 != 'h' and l2 != 't' and l2 != 'f':
                print('Please type in the correct language.')
                sleep(1)
                eq()
                continue
            else:
                if l2 == 'h':
                    l2n = 'Hindi'
                elif l2 == 't':
                    l2n = 'Telugu'
                elif l2 == 'f':
                    l2n = 'French'
                # Marks
                while True:
                    sub = input(f'How much did {e} get in Maths(out of 100)? ')
                    sleep(1)
                    sub1 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub1 = int(sub)
                    if sub1 == '200':
                        continue
                    if sub1 > 100 or sub1 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in Science(out of 100)? ')
                    sleep(1)
                    sub2 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub2 = int(sub)
                    if sub2 == '200':
                        continue
                    if sub2 > 100 or sub2 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in Social Science(out of 100)? ')
                    sleep(1)
                    sub3 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub3 = int(sub)
                    if sub3 == '200':
                        continue
                    if sub3 > 100 or sub3 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in English(out of 100)? ')
                    sleep(1)
                    sub4 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub4 = int(sub)
                    if sub4 == '200':
                        continue
                    if sub4 > 100 or sub4 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in {l2n}(out of 100)? ')
                    sleep(1)
                    sub5 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub5 = int(sub)
                    if sub5 == '200':
                        continue
                    if sub5 > 100 or sub5 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in Computers(out of 100)? ')
                    sleep(1)
                    sub6 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub6 = int(sub)
                    if sub6 == '200':
                        continue
                    if sub6 > 100 or sub6 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue
                    break
                break

        elif c >= 5 and c <= 8:
            final = 3
            l2 = input(f'What is {e}\'s second language(Type in "t" for Telugu, "h" for Hindi, "f" for French)? ').lower()
            sleep(1)
            # Checking Language
            if l2 != 'h' and l2 != 't' and l2 != 'f':
                print('Please type in the correct language.')
                sleep(1)
                eq()
                continue
            l3 = input(f'What is {e}\'s third language(Type in "s" for Sanskrit, "h" for Hindi, "t" for Telugu, "f" for French)? ').lower()
            sleep(1)
            # Checking Language
            if l3 != 's' and l3 != 'h' and l3 != 't' and l3 != 'f':
                print('Please type in the correct language.')
                sleep(1)
                eq()
                continue
            if l3 == l2:
                print('The second and third language cannot be the same.')
                sleep(1)
                eq()
                continue
            else:
                if l2 == 'h':
                    l2n = 'Hindi'
                elif l2 == 't':
                    l2n = 'Telugu'
                elif l2 == 'f':
                    l2n = 'French'

                if l3 == 's':
                    l3n = 'Sanskrit'
                elif l3 == 'h':
                    l3n = 'Hindi'
                elif l3 == 't':
                    l3n = 'Telugu'
                elif l3 == 'f':
                    l3n = 'French'
                # Marks
                while True:
                    sub = input(f'How much did {e} get in Maths(out of 100)? ')
                    sleep(1)
                    sub1 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub1 = int(sub)
                    if sub1 == '200':
                        continue
                    if sub1 > 100 or sub1 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in Science(out of 100)? ')
                    sleep(1)
                    sub2 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub2 = int(sub)
                    if sub2 == '200':
                        continue
                    if sub2 > 100 or sub2 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in Social Science(out of 100)? ')
                    sleep(1)
                    sub3 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub3 = int(sub)
                    if sub3 == '200':
                        continue
                    if sub3 > 100 or sub3 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in English(out of 100)? ')
                    sleep(1)
                    sub4 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub4 = int(sub)
                    if sub4 == '200':
                        continue
                    if sub4 > 100 or sub4 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in {l2n}(out of 100)? ')
                    sleep(1)
                    sub5 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub5 = int(sub)
                    if sub5 == '200':
                        continue
                    if sub5 > 100 or sub5 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue
                    sub = input(f'How much did {e} get in {l3n}(out of 100)? ')
                    sleep(1)
                    sub7 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub7 = int(sub)
                    if sub7 == '200':
                        continue
                    if sub7 > 100 or sub7 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue
                    sub = input(f'How much did {e} get in Computers(out of 100)? ')
                    sleep(1)
                    sub6 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub6 = int(sub)
                    if sub6 == '200':
                        continue
                    if sub6 > 100 or sub6 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue
                    break
                break

        elif c > 8 and c <= 10:
            final = 4
            l2 = input(f'What is {e}\'s second language(Type in "t" for Telugu, "h" for Hindi, "f" for French,)? ').lower()
            sleep(1)
            # Checking Language
            if l2 != 'h' and l2 != 't' and l2 != 'f':
                print('Please type in the correct language.')
                sleep(1)
                eq()
                continue
            else:
                if l2 == 'h':
                    l2n = 'Hindi'
                elif l2 == 't':
                    l2n = 'Telugu'
                elif l2 == 'f':
                    l2n = 'French'
                # Marks
                while True:
                    sub = input(f'How much did {e} get in Maths(out of 100)? ')
                    sleep(1)
                    sub1 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub1 = int(sub)
                    if sub1 == '200':
                        continue
                    if sub1 > 100 or sub1 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in Science(out of 100)? ')
                    sleep(1)
                    sub2 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub2 = int(sub)
                    if sub2 == '200':
                        continue
                    if sub2 > 100 or sub2 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in Social Science(out of 100)? ')
                    sleep(1)
                    sub3 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub3 = int(sub)
                    if sub3 == '200':
                        continue
                    if sub3 > 100 or sub3 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in English(out of 100)? ')
                    sleep(1)
                    sub4 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub4 = int(sub)
                    if sub4 == '200':
                        continue
                    if sub4 > 100 or sub4 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in {l2n}(out of 100)? ')
                    sleep(1)
                    sub5 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub5 = int(sub)
                    if sub5 == '200':
                        continue
                    if sub5 > 100 or sub5 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue

                    sub = input(f'How much did {e} get in Computers(out of 100)? ')
                    sleep(1)
                    sub6 = '200'
                    for index, var in enumerate(sub):
                        if sub[index] in all:
                            print('Please enter the correct marks')
                            sleep(1)
                            eq()
                            break
                    else:
                        sub6 = int(sub)
                    if sub6 == '200':
                        continue
                    if sub6 > 100 or sub6 < 0:
                        print('Please type in marks out of 100.')
                        sleep(1)
                        eq()
                        continue
                    break
                break

        elif c > 10 and c <= 12:
            final = 5
            st = input(f'What stream is {e} in(Type in either "mpc" or "cec")? ').lower()
            sleep(1)
            # Checking Subjects
            if st != 'mpc' and st != 'cec':
                print('Please choose the correct stream.')
                sleep(1)
                eq()
                continue
            extsub = input(f'What is {e}\'s 5th core(Type in either "IP", "P" for Psychology, "PE", "M" for Maths, "A" For Fine Arts.)? ').lower()
            sleep(1)
            # Checking Subjects
            if extsub != 'ip' and extsub != 'p' and extsub != 'm' and extsub != 'a':
                print('Please type in the correct 5th core.')
                sleep(1)
                eq()
                continue
            else:
                if extsub == 'm' and st == 'mpc':
                    print('The main stream and 5th core cannot have the same subject.')
                    sleep(1)
                    eq()
                    continue
                else:
                    st4 = 'English'
                    if st == 'mpc':
                        st1 = 'Maths'
                        st2 = 'Physics'
                        st3 = 'Chemistry'
                    elif st =='cec':
                        st1 = 'Commerce'
                        st2 = 'Economics'
                        st3 = 'Business Studies'
                    if extsub == 'ip':
                        st5 = 'IP'
                    elif extsub == 'p':
                        st5 = 'Psychology'
                    elif extsub == 'm':
                        st5 = 'Maths'
                    elif extsub == 'a':
                        st5 = 'Fine Arts'
                    while True:
                        sub1 = int(input(f'How much did {e} get in {st1}(out of 100)? '))
                        sleep(1)
                        if sub1 > 100 or sub1 < 0:
                            print('Please type in marks out of 100.')
                            sleep(1)
                            eq()
                            continue
                        sub2 = int(input(f'How much did {e} get in {st2}(out of 100)? '))
                        sleep(1)
                        if sub2 > 100 or sub2 < 0:
                            print('Please type in marks out of 100.')
                            sleep(1)
                            eq()
                            continue
                        sub3 = int(input(f'How much did {e} get in {st3}(out of 100)? '))
                        sleep(1)
                        if sub3 > 100 or sub3 < 0:
                            print('Please type in marks out of 100.')
                            sleep(1)
                            eq()
                            continue
                        sub4 = int(input(f'How much did {e} get in {st4}(out of 100)? '))
                        sleep(1)
                        if sub4 > 100 or sub4 < 0:
                            print('Please type in marks out of 100.')
                            sleep(1)
                            eq()
                            continue
                        sub5 = int(input(f'How much did {e} get in {st5}(out of 100)? '))
                        sleep(1)
                        if sub5 > 100 or sub5 < 0:
                            print('Please type in marks out of 100.')
                            sleep(1)
                            eq()
                            continue
                        break
                    break

    # Returning Output
    if final == 1:
        return {'sub1': sub1, 'sub2': sub2, 'sub3': sub3, 'sub4': sub4, 'sub5': sub5, 'grade': c}, c, final, st, st5, l3n, l2n
    elif final == 2:
        return {'sub1': sub1, 'sub2': sub2, 'sub3': sub3, 'sub4': sub4, 'sub5': sub5, 'sub6': sub6, 'grade': c}, c, final, st, st5, l3n, l2n
    elif final == 3:
        return {'sub1': sub1, 'sub2': sub2, 'sub3': sub3, 'sub4': sub4, 'sub5': sub5, 'sub7' : sub7, 'sub6': sub6, 'grade': c}, c, final, st, st5, l3n, l2n
    elif final == 4:
        return {'sub1': sub1, 'sub2': sub2, 'sub3': sub3, 'sub4': sub4, 'sub5': sub5, 'sub6': sub6, 'grade': c}, c, final, st, st5, l3n, l2n
    elif final == 5:
        return {'sub1': sub1, 'sub2': sub2, 'sub3': sub3, 'sub4': sub4, 'sub5': sub5, 'grade': c}, c, final, st, st5, l3n, l2n
