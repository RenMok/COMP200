# This program uses a while loop to make the user guess the password "hello". Once correctly guessed, it uses an if/else loop to input based on lists of names.
author_list = ["Renfred", "renfred", "Renfred Mok", "Ren", "ren"]
celeb_list = ["Cher", "cher", "Madonna", "madonna"]
print ("Program Author: Renfred Mok")
print ("ID#: 3451103 ")
print ("Program 3 - Loops and If Conditions")
print ()

password = 1
while password != "hello":
    password = input("Password? ")
    if password == "hello":
        print("Welcome to the second half of the program")
        name = input("What is your name? ")
        if name in author_list:
            print("What a great name!")
        elif name in celeb_list:
            print("May I have your autograph, please?")
        else:
            print(name + ", that's a nice name.")


    