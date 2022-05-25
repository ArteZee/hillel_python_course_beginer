# user age input
age_of_birthday: str = input()

if age_of_birthday.isdigit() == False:
    print("Введите число ")
else:
    # Change value from str to int
    age_of_birthday = int(age_of_birthday)
    if age_of_birthday == 21:
        print("You should visit Holland.")
    elif age_of_birthday > 21:
        print("You should visit Vietnam.")
    else:
        print("Travel everywhere")
