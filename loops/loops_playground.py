for num in range(10):
    print(num)
for num in range(1,11):
    print(num)

print()

for num in range(0, 11, 2):
    print(num)

for num in range (0, 101):
    print (num)
for num in range (0,101,5):
    print (num)

chilli_wishlist = [
    "igloo", # bed
    ["donut toy", "tennis ball","croodile"],
    "chicken","peanut butter", # treats
    "cardboard box","kong" # puzzles
]
for item in chilli_wishlist:
    print(item)
for item in chilli_wishlist:
    print(f"Chilli wants: {item}")
guess = ""
while guess != "a":
    guess = input("Guess a letter:" )

counter = 0
while counter <= 5:
    print(counter)
    counter = counter + 1