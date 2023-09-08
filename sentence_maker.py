import random

character_height = ['tall', 'short']
character_type = ['man', 'woman', 'person']
character_pronoun = ["He is", "She is", "They are"]


pronoun = random.choice(character_pronoun)
height = random.choice(character_height)
gender = random.choice(character_type)
print(f"{pronoun} a {height} {gender} ")


