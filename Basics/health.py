import random

health = 50
difficulty = 3

# Sets the potion health inversely proportional to difficulty variable
potionHealth = int(random.randint(25,50)/difficulty)

# Adds the potion health to current health and prints new health
health = health + potionHealth
print(health)