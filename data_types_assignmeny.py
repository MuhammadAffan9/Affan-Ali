
print("Let's imagine your future!")

name = input("What's your name? ")
age = int(input("How old are you? "))
future_age = age + 5
print(f"\nHi {name}! In 5 years, you'll be {future_age} years old!")

height = float(input("\nHow tall are you in meters? (Like 1.3) "))
print(f"Wow! You're {height} meters tall! You're growing fast!")

print("\nLet's go shopping!")
item = input("What do you want to buy? ")
price = float(input(f"How much does one {item} cost? $"))
quantity = int(input(f"How many {item}s do you want? "))

total = price * quantity
print(f"\n📦 Awesome {name}! You bought {quantity} {item}s.")
print(f"💰 Total: ${total:.2f}")
print("Thanks for shopping with us!")