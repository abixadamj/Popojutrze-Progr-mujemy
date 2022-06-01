actual_year = 2022
birth = 1974
my_name = "Beata"

print(f"Hi {my_name}, we'll try to compute your age ;-)")
age = actual_year - birth

if age >= 18:
    print(f"Oh, I see, {my_name} - you are an adult now.")
    print(f"You are {age} years old.")
else:
    print(f"You are young - {age} years old.")


if my_name.endswith("a"):
    print(f"I guess {my_name} - you are a woman.")
    if my_name.lower() == "barnaba":
        print(f"But your name: {my_name} is an exception - you are a man!")
else:
    print("You probably are a man...")
print("That is all - see you next time!")
