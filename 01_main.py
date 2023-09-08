
import random


def statement_generator(text, decoration):

    # Make string with five characters
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""
# lists


menu = ['French Toast', '?', '?', '?']
character_height = ['tall', 'short', '']
character_type = ['man', 'woman', 'person']


statement_generator("Crow's Cookery", "*")

# Main Routine

print("Hello, and welcome to Crow's Cookery! I hope you have a great time!")
print()

name = input("To start, please tell us your name")

print()
print(f"Nice to meet you{name}!")
print()

print("Let's choose your cooking level")

cooking_level = int(input("Are you (1) Beginner (2) Intermediate or (3) Advanced? "))
text_ok = [1, 2, 3]
if cooking_level not in text_ok:
    print("I'm sorry. Please choose 1, 2, or 3")

else:
    print ()
    print("Ok, Level Chosen")

statement_generator("Starting Game", "*")

statement_generator("Day One", "-")

# start game
print()
print("Menu:")
for item in menu:
    print(item)

print()
print("*The bell rings and Your first customer walks in*")
print()
height = random.choice(character_height)
gender = random.choice(character_type)
print(f"They are a {height} {gender} ")





















