# if int(age) < 18:
#     print("Sorry, you are too young to drive this car. Powering off")
# elif int(age) > 18:
#     print("Powering On. Enjoy the ride!")
# elif int(age) == 18:
#     print("Congratulations on your first year of driving. Enjoy the ride!")

# 1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

# 2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
# checkDriverAge(92);
# it returns "Powering On. Enjoy the ride!"
# also make it so that the default age is set to 0 if no argument is given.


def checkDriverAge(age):
    if age < 18:
        return "Sorry, you are too young to drive this car. Powering off"
    elif int(age) > 18:
        return "Powering On. Enjoy the ride!"
    elif int(age) == 18:
        return "Congratulations on your first year of driving. Enjoy the ride!"


age = input("how old are you?")
age = int(age) if age else 0
print(checkDriverAge(age))


# Highest even
def highest_even(li):
    even_list = []
    for i in li:
        if i % 2 == 0:
            even_list.append(i)

    return max(even_list)


print(highest_even([10, 2, 3, 4, 8, 11]))
