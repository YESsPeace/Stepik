import random
answers = ['Yes', 'No', 'ъэъ', 'Ho-ho-ho']

print("Ben.")

n = 1
while n:
    question = input("-")
    print("-", random.choice(answers), sep= "")
    print()
