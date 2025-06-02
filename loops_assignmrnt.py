
print("Welcome to Loop World! Let's explore loops together!\n")

print("🌈 Task 1: Counting 1 to 10 with a rocket launch!")
for number in range(1, 11):
    print(f"🚀 {number}...")
print("Blast off! 🌌\n")

print("🐢 Task 2: Slow turtle counting 1 to 5")
count = 1
while count <= 5:
    print(f"🐢 Turtle step {count}")
    count += 1
print("Turtle reached home! 🏠\n")

start = int(input("🎮 Task 3: Let's countdown! Enter a number: "))
print(f"Countdown from {start}:")
while start > 0:
    print(f"🔔 {start}")
    start -= 1
print("Happy New Year! 🎉\n")

print("🧮 Task 4: Mini Multiplication Magic (1-3)")
for first in range(1, 4):
    for second in range(1, 4):
        result = first * second
        print(f"✨ {first} x {second} = {result}")
    print("---")
print("Math magic complete! 🎩\n")

print("🚧 Task 5: Numbers 0-10 (stopping at 6)")
for num in range(0, 11):
    if num == 6:
        print("⛔ Whoops! Hit 6 - stopping!")
        break
    print(f"➡ {num}")
print("Break time! 🥪\n")

print("⏩ Task 6: Counting 0-5 (skipping 3)")
for num in range(0, 6):
    if num == 3:
        print("👻 Skipped the spooky 3!")
        continue
    print(f"✅ {num}")
print("No threes allowed! ❌\n")

word = input("🔤 Bonus Task: Enter a fun word: ")
print(f"Spelling '{word}':")
for letter in word:
    print(f"🔡 {letter.upper()}")
print(f"Word spelled! ✨ Total letters: {len(word)}")