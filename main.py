import string
import random


def strings():
    s_number_1 = string.ascii_letters
    s_number_2 = string.digits
    s_number_3 = string.punctuation
    s_list = []
    s_list.extend(list(s_number_1 + s_number_2 + s_number_3))
    return s_list


def password_generator():
    char = strings()
    while 1:
        while True:
            try:
                password_lenght = int(input("What is you desired password lenght? : "))
                password_count = int(input("How many password do you want? : "))
                break
            except ValueError:
                print("Sorry! this is not a valid number ..PLz try again")
        for i in range(0, password_count):
            password = ""
            for j in range(0, password_lenght):
                password_char = random.choice(char)
                password = password + password_char
            print("Your password is   " + password)
        play = input("do want to it again?(yes/no) : ").lower()
        if play != "yes":
            print("byeee")
            break


password_generator()