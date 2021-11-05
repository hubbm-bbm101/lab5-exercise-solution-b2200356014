e_mail = input("Enter your e-mail address:")
is_valid = False
while not is_valid:
    if "@" in e_mail:
        if "." in e_mail:
            print("Your e-mail is valid.")
            is_valid = True
        else:
            e_mail = input("Please, enter a valid e-mail:")
    else:
        e_mail = input("Please, enter a valid e-mail:")
