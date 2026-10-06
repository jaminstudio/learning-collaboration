import random


words = ["moon", "sun", "star", "sky", "cloud","rain","wind",]
word = random.choice(words)
num = random.randint(1,99)
sym = random.choice(random.punctuation)

print(f"Your random password: {word.capitalize()}{num}{sym}")


