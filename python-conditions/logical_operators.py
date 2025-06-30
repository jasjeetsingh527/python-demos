# ==, != , >, <, >=, <=, and, or, not

is_magician = False
is_expert = True

# check if magician and expert
if is_magician and is_expert:
    print("You are a master magician.")

# check if magician but not expert
elif is_magician and not is_expert:
    print("At least you're getting there.")

# check if not magician
else:
    print("You need magic powers.")
