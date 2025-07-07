while True:
    try:
        age = int(input("What's your age? "))
        10 / age
    except ValueError:
        print("Please enter a number.")
    except ZeroDivisionError:
        print("Please enter a number higher than 0.")
    else:
        print("Thank you!")
        break
    finally:
        print("Finally")
