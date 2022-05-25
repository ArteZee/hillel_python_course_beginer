print("Welcome to the club buddy !")

# get user nickname
user_name = input("How to call you ? \n")

# get sex of user
user_sex = input("What`s your gender ? \n"
                 "Put 'm' if - Male \n"
                 "Put 'f' if - Female\n").capitalize()
# get age of user
user_age = int(input("How old are you ? \n"))
#  for  Женя
if user_name == "Женя":
    print("Advice you to see the 'TENET'")
else:
    # for admin
    if user_name == "admin":
        print("Welcome", "my lord !", sep=",", end="\n")
    #  for Male and from 10 to 14  or older than 30
    if 10 < user_age < 14 and user_sex == "M" or user_age > 30 and user_sex == "M":
        print("Advice you to see the 'Star Wars' or 'The Mandalorian'")
    # for Female from 22 to 32
    elif 22 < user_age < 32 and user_sex == "F":
        print("Advice you to see the 'Transformers'")
    #  for Female younger than 16
    elif  user_age < 16 and user_sex == "F":
        print("Advice you to see the 'Insurgent'")
    #  for Male younger than 11
    elif user_age < 11 and user_sex == "M":
        print("Advice you to see the 'TMNT'")
    # for Guido
    elif user_name == "Guido":
        print("Thank you very much", end="!")
