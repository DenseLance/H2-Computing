def option(prompt):
    user_input = input(prompt)
    while not validate(user_input):
        user_input = input(prompt)
    return user_input

def validate(user_input):
    if len(user_input) == 0: # presence check
        print("Presence check failed.")
        return False
    elif not user_input.isdigit(): # type check
        print("Type check failed.")
        return False
    elif int(user_input) < 1 or int(user_input) > 4: # range check
        print("Range check failed.")
        return False
    else:
        return True

def menu():
    done = False
    while not done:
        menu = \
             """
            [1] SAY HI
            [2] CALL THE AMBULANCE
            [3] OwO
            [4] QUIT
            """
        user_input = int(option("User input: "))
        if user_input == 1:
            print("Hello there!")
        elif user_input == 2:
            print("Call the AMBULANCE! But not for ME!")
        elif user_input == 3:
            print("OwO")
        else:
            done = True
        print()

menu()
