# %%
###################! Imports ###################
# ? For Generating Password
import string

# ? For Running Commands
from os import name, popen, system

# ? For Generating Password
from random import choice as randchoice

# ? For Pausing the Script
from time import sleep

# ? For Connecting to MySQL
import pymysql

# ? For Copying to Clipboard
import pyperclip


###################! Functions ###################
######? Database Checking ######
def db_check():
    #####* Variables #####
    result = []

    #####* Going Through Databases #####
    cur.execute("show databases")
    res = cur.fetchall()
    for _ in res:
        result.append(_[0])

    #####* Checking if database exists #####
    if "manager" not in result:
        cur.execute("create database Manager")

    return "Manager"


######? Table Checking ######
def table_check(d):
    #####* Variables #####
    t = "passwords"
    result = []

    #####* Going Through Database #####
    cur.execute(f"show tables from {d}")
    res = cur.fetchall()
    for _ in res:
        result.append(_[0])

    #####* Checking if database exists #####
    if t not in result:
        cur.execute(
            f"Create table {d}.{t}(IndexNo int, Name varchar(244), Email varchar(244), Username varchar(244), Password varchar(244))"
        )

    return t


######? Master Password ######
def MasterPass():
    #####* Variables #####
    i = 0

    #####* Clearing The Screen #####
    sleep(1)
    system("clear|cls")
    print("-" * 100)
    print("-" * 10, "This is a Password Manager")
    print("-" * 100)
    print()

    #####* Checking if Master Password is Saved #####
    try:
        if name == "nt":
            chk = popen("cd %userprofile% && dir").read()
            CWD = popen("cd %userprofile% && chdir").read()
            CWD = CWD[:-1] + "\\"
            if "mpformanager" in chk:
                MP = popen("cd %userprofile% && more mpformanager").read()
                MP = MP[:-1]
                ###? Asking for Master Password ###
                while True:
                    mp = input("Please enter your master password: ")
                    i += 1
                    if mp == MP:
                        break
                    if i == 3:
                        print(
                            "You have had too many unsuccessful attempts, please try again."
                        )
                        quit()
            else:
                raise ValueError
        elif name == "posix":
            chk = popen("ls ~").read()
            if "mpformanager" in chk:
                MP = popen("cd ~/mpformanager").read()
                MP = MP[:-1]
                ###? Asking for Master Password ###
                while True:
                    mp = input("Please enter your master password: ")
                    if mp == MP:
                        break
            else:
                raise ValueError
    except ValueError:
        #####* Running this if Master Password not saved #####
        while True:
            mp = input(
                f"As this is your first time running this script, please enter a Master Password: "
            )
            mp2 = input(f"Please enter it again: ")
            if mp != mp2:
                continue
            break
        file = open(CWD + "mpformanager", "w")
        file.write(mp)
        file.close()


######? Generating Passwords ######
def GenPass(p):
    genop = ""
    while True:
        gen = input("Do you want to generate a password? ").lower()
        if gen == "yes":
            while True:
                try:
                    genlen = int(input("How long should the password be? "))
                    if genlen <= 0:
                        raise ValueError
                    break
                except:
                    print("Please enter a valid positive number.")
            for _ in range(genlen):
                genop += randchoice(
                    string.ascii_letters + string.digits + string.punctuation
                )

            print(f"The generated password is {genop}")
            return genop
        elif gen == "no":
            return input(p)
        else:
            print("Please only enter either yes or no.")


######? Adding Entry ######
def AddEntry(d, t):
    #####* Variables #####
    result = []
    NameResult = []

    #####* Clearing the Screen #####
    system("clear|cls")
    print("-" * 100)
    print("-" * 10, "This is a Password Manager")
    print("-" * 100)
    print()

    #####* Going Through Table #####
    cur.execute(f"select * from {d}.{t}")
    res = cur.fetchall()
    for _ in res:
        result.append(_)
    cur.execute(f"select Name from {d}.{t}")
    res = cur.fetchall()
    if len(res) != 0:
        for _ in res:
            _ = _[0].lower()
            NameResult.append(_)

    #####* Getting Values #####
    while True:
        name = input("What do you want the entry to be called? ")
        if name == "":
            print("Name cannot be left empty.")
            continue
        if name.lower() in NameResult:
            print("That name already exists.")
            continue
        break
    email = input("What is the Email ID(can be left empty)? ")
    usrname = input("What is the Username(can be left empty)? ")
    passwd = GenPass("What is the Password? ")

    #####* Adding Values to Table #####
    cur.execute(
        f"insert into {d}.{t} values({len(result) + 1}, '{name}', '{email}', '{usrname}', '{passwd}')"
    )
    conn.commit()
    print(f"The entry for {name} has been successfully added!")
    sleep(1)


######? Editting Entry ######
def EditEntry(d, t):
    #####* Variables #####
    result = []
    Name = "-"
    Email = "-"
    Username = "-"
    Passwd = "-"

    #####* Going Through Table #####
    cur.execute(f"select * from {d}.{t}")
    res = cur.fetchall()
    for _ in res:
        result.append(_)

    #####* Printing Options #####
    while True:
        ###? Clearing the Screen ###
        sleep(1)
        system("clear|cls")
        print("-" * 100)
        print("-" * 10, "This is a Password Manager")
        print("-" * 100)
        print()
        ###? Options ###
        for index, value in enumerate(result):
            print(f"Press {index + 1} for {value[1]}")
        print("Press 0 to quit")
        choice = input("Which entry do you want to delete? ")
        # ? Checking if choice is valid integer
        if choice.isdigit():
            choice = int(choice)
            if choice == "0":
                quit()
            else:
                if 0 > choice or choice > index + 1:
                    sleep(1)
                    system("clear|cls")
                    print("-" * 100)
                    print("-" * 10, "This is a Password Manager")
                    print("-" * 100)
                    print()
                    print("Please enter a valid choice.")
                    continue
            break

    #####* Getting Values #####
    ###? Name ###
    while True:
        name = input("Do you want to change the name? ").lower()
        if name not in ["yes", "no"]:
            print('Please enter only "yes" and "no"')
            continue
        elif name == "yes":
            while True:
                Name = input("What should the name be? ")
                cur.execute(f"update {d}.{t} set Name='{Name}' where IndexNo={choice}")
                break
        break
    ###? Email ###
    while True:
        email = input("Do you want to change the email? ").lower()
        if email not in ["yes", "no"]:
            print('Please enter only "yes" and "no"')
            continue
        elif email == "yes":
            while True:
                Email = input("What should the email be? ")
                cur.execute(
                    f"update {d}.{t} set Email='{Email}' where IndexNo={choice}"
                )
                break
        break
    ###? Username ###
    while True:
        username = input("Do you want to change the Username? ").lower()
        if username not in ["yes", "no"]:
            print('Please enter only "yes" and "no"')
            continue
        elif username == "yes":
            while True:
                Username = input("What should the username be? ")
                cur.execute(
                    f"update {d}.{t} set Username='{Username}' where IndexNo={choice}"
                )
                break
        break
    ###? Password ###
    while True:
        passwd = input("Do you want to change the password? ").lower()
        if passwd not in ["yes", "no"]:
            print('Please enter only "yes" and "no"')
            continue
        elif passwd == "yes":
            while True:
                Passwd = GenPass("What should the password be? ")
                cur.execute(
                    f"update {d}.{t} set Password='{Passwd}' where IndexNo={choice}"
                )
                break
        break
    if Name == "-" and Email == "-" and Username == "-" and Passwd == "-":
        print("The entry has not been modified.")
    else:
        conn.commit()
        print("The entry has been successfully modified!")
    sleep(1)


######? Deleting Entry ######
def DelEntry(d, t):
    #####* Variables #####
    result = []
    Names = []

    #####* Going Through Table #####
    cur.execute(f"select * from {d}.{t}")
    res = cur.fetchall()
    for _ in res:
        result.append(_)

    #####* Printing Options #####
    while True:
        ###? Clearing the Screen ###
        sleep(1)
        system("clear|cls")
        print("-" * 100)
        print("-" * 10, "This is a Password Manager")
        print("-" * 100)
        print()
        ###? Options ###
        for index, value in enumerate(result):
            print(f"Press {index + 1} for {value[1]}")
        print("Press 0 to quit")
        choice = input("Which password do you want to delete? ")
        # ? Checking if choice is valid integer
        if choice.isdigit():
            choice = int(choice)
            if choice == "0":
                quit()
            else:
                if 0 > choice or choice > index + 1:
                    sleep(1)
                    system("clear|cls")
                    print("-" * 100)
                    print("-" * 10, "This is a Password Manager")
                    print("-" * 100)
                    print()
                    print("Please enter a valid choice.")
                    continue
            break

    #####* Confirmation #####
    while True:
        cur.execute(f"select Name from {d}.{t} where IndexNo={choice}")
        name = cur.fetchall()[0][0]
        conf = input(f"Are you sure you want to delete the entry for {name}? ").lower()
        if conf not in ["yes", "no"]:
            continue
        elif conf == "yes":
            cur.execute(f"delete from {d}.{t} where IndexNo={choice}")
            conn.commit()
            ###? Setting Proper Index Numbers ###
            cur.execute(f"select Name from {d}.{t}")
            names = cur.fetchall()
            for _ in names:
                Names.append(_[0])
            for index, val in enumerate(Names):
                cur.execute(
                    f"update {d}.{t} set IndexNo={index + 1} where Name='{val}'"
                )
            conn.commit()
            ###? Confirmation ###
            print(f"The entry for {name} has been successfully deleted!")
            sleep(1)
            break
        elif conf == "no":
            break


######? Copying Entry ######
def CopyEntry(d, t):
    #####* Variables #####
    result = []

    #####* Going Through Table #####
    cur.execute(f"select * from {d}.{t}")
    res = cur.fetchall()
    for _ in res:
        result.append(_)

    #####* Printing Options #####
    while True:
        ###? Clearing the Screen ###
        sleep(1)
        system("clear|cls")
        print("-" * 100)
        print("-" * 10, "This is a Password Manager")
        print("-" * 100)
        print()
        ###? Options ###
        for index, value in enumerate(result):
            print(f"Press {index + 1} for {value[1]}")
        print("Press 0 to quit")
        choice = input("Which entry do you want to copy? ")
        # ? Checking if choice is valid integer
        if choice.isdigit():
            choice = int(choice)
            if choice == "0":
                quit()
            else:
                if 0 > choice or choice > index + 1:
                    sleep(1)
                    system("clear|cls")
                    print("-" * 100)
                    print("-" * 10, "This is a Password Manager")
                    print("-" * 100)
                    print()
                    print("Please enter a valid choice.")
                    continue
            break
    #####* Copying to Clipboard #####
    ###? Getting Name ###
    cur.execute(f"select Name from {d}.{t} where IndexNo={choice}")
    name = cur.fetchall()[0][0]
    while True:
        ###? Getting What User Wants to Copy to Clipboard ###
        conf = input("What do you want to copy(email, username, password)? ").lower()
        if conf not in ["email", "username", "password"]:
            continue

        ###? Email ###
        elif conf == "email":
            cur.execute(f"select Email from {d}.{t} where IndexNo={choice}")
            result = cur.fetchall()[0][0]
            if result == "":
                print(f"The email in {name} does not exist.")
                continue
            pyperclip.copy(result)
            print("The email has been successfully copied to your clipboard!")
            sleep(1)
            break

        ###? Username ###
        elif conf == "username":
            cur.execute(f"select Username from {d}.{t} where IndexNo={choice}")
            result = cur.fetchall()[0][0]
            if result == "":
                print(f"The Username in {name} does not exist.")
                continue
            pyperclip.copy(result)
            print("The username has been successfully copied to your clipboard!")
            sleep(1)
            break

        ###? Password ###
        elif conf == "password":
            cur.execute(f"select Password from {d}.{t} where IndexNo={choice}")
            result = cur.fetchall()[0][0]
            if result == "":
                print(f"The Password in {name} does not exist.")
                continue
            pyperclip.copy(result)
            print("The password has been successfully copied to your clipboard")
            sleep(1)
            break


###################! Connecting To SQL ###################
#####* Checking If password is saved #####
try:
    if name == "nt":
        chk = popen("cd %userprofile% && dir").read()
        CWD = popen("cd %userprofile% && chdir").read()
        CWD = CWD[:-1] + "\\"
        if "formanager" in chk:
            p = popen("cd %userprofile% && more formanager").read()
            p = p[:-1]
        else:
            raise ValueError
    elif name == "posix":
        chk = popen("ls ~").read()
        if "formanager" in chk:
            p = popen("cd ~/formanager").read()
            p = p[:-1]
        else:
            raise ValueError
except ValueError:
    #####* Clearing The Screen #####
    sleep(1)
    system("clear|cls")
    print("-" * 100)
    print("-" * 10, "This is a Password Manager")
    print("-" * 100)
    print()

    #####* Running this if password is not saved #####
    while True:
        p = input("Please type in your SQL Password: ")
        try:
            ###? Connecting ###
            conn = pymysql.connect(user="root", host="localhost", password=p)
            cur = conn.cursor()
            ###? Saving password ###
            a = open(CWD + "formanager", "w")
            a.write(p)
            a.close()
            break
        except:
            print("The password was wrong, please try again.")
###? Connecting ###
conn = pymysql.connect(user="root", host="localhost", password=p)
cur = conn.cursor()

###################! Printing Options ###################
#####? Checks #####
# * Checking if the database required exists
database = db_check()
# * Checking if the table required exists
table = table_check(database)
# * Master Password
MasterPass()

#####? Printing Options #####
while True:
    ####* Printing what the script does ####
    system("clear|cls")
    print("-" * 100)
    print("-" * 10, "This is a Password Manager")
    print("-" * 100)
    print()
    ####* Printing Options ####
    print("Press 1 to Add Entry")
    print("Press 2 to Edit Entry")
    print("Press 3 to Delete an Entry")
    print("Press 4 to Copy an Entry")
    print("Press 0 to quit")
    choice = input("What is your choice? ")
    # ? Checking if choice is valid integer
    if choice.isdigit():
        choice = int(choice)
        if 0 > choice or choice >= 5:
            continue

    #######? Calling Functions #######
    if choice == 0:
        quit()
    elif choice == 1:
        AddEntry(database, table)
    elif choice == 2:
        EditEntry(database, table)
    elif choice == 3:
        DelEntry(database, table)
    elif choice == 4:
        CopyEntry(database, table)

# %%
""
