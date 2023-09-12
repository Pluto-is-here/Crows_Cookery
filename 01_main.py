

import random
import simple_colors 



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


menu = [ 'French Toast', '?', '?', '?']

character_height = ['tall', 'short', '']
character_type = ['man', 'woman', 'person']
character_personality = ['a gold tooth', 'cool glasses', 'a mischevous smile', 'a funky hat',"bushy hair", 'striking blue eyes' ]

speech_option = ['Hullo.', 'Hey!', 'Hello.', 'Hi!' ]


statement_generator("Crow's Cookery", "*")

# Main Routine

print("Hello, and welcome to Crow's Cookery! I hope you have a great time!")
print()

name = input("To start, please tell us your name: ")

print()
print(f"Nice to meet you {name}!")
print()


# print("Let's choose your cooking level")


# cooking_level = int(input("Are you (1) Beginner (2) Intermediate or (3) Advanced? "))
# text_ok = [1, 2, 3]
# if cooking_level not in text_ok:
#     print("I'm sorry. Please choose 1, 2, or 3")

# else:
#     print ()
#     print("Ok, Level Chosen")

statement_generator("Starting Game", "*")

statement_generator("Day One", "-")

# start game

level = 0 

print()
print("Menu:")
for item in menu:
    print(item)

print()
print("*The bell rings and Your first customer walks in*")
print()

character_height = ['tall', 'short']
character_type = ['man', 'woman', 'person']
character_pronoun = ["He is", "She is", "They are"]

character_num = random.randint(0,len(character_type)-1)
pronoun = character_pronoun[character_num]
gender = character_type[character_num]

height = random.choice(character_height)
descriptor = random.choice(character_personality)

print(f"{pronoun} a {height} {gender} with {descriptor} ")
print ()


greeting = random.choice(speech_option)
food_num = random.randint(0,level)
food = menu[food_num]

print (simple_colors.magenta(f"> {greeting} May I have a {food}? "))
print()
print()
print(f"Ok, {name}! Time to start cooking. Cooking is a skill, so let's solve some equations.")

equation_num1 = random.randint(0,9)
equation_num2 = random.randint(0,9)

equation = f"{equation_num1} + {equation_num2}"
 # answer = equation_num1 + equation_num2
print ()
answer = float(input(f"First, Dip the bread in the egg. What's {equation}? "))

if answer != equation_num1 + equation_num2:
    print()
    print ("I'm sorry, that's wrong. Please try again.")

else:
    print ("Correct!") 

























