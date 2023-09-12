import random

character_height = ['tall', 'short']
character_type = ['man', 'woman', 'person']
character_pronoun = ["He is", "She is", "They are"]

character_num = random.randint(0,len(character_type)-1)
pronoun = character_pronoun[character_num]
gender = character_type[character_num]

height = random.choice(character_height)

print(f"{pronoun} a {height} {gender} ")


