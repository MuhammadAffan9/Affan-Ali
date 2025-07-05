
print("Welcome this is my first loop assignment\n")

print(" Task 1: Counting 1 to 10 with a rocket launch!")
for number in range(1, 11):
    print(f" {number}...")                # reocket will launch to the moon
print("Blast off!\n")

print(" Task 2: Slow turtle counting 1 to 5")
count = 1
while count <= 5:
    print(f" Turtle step {count}")          
    count += 1                          #finally turtle  reached
print("finally he did it \n")

start = int(input("Task 3: Let's countdown! Enter a number: "))
print(f"Countdown from {start}:")
while start > 0:
    print(f" {start}")                            
    start -= 1
print("Happy 2025 \n")

print(" Task 4: Mini Multiplication Magic (1-3)")
for first in range(1, 4):
    for second in range(1, 4):
        result = first * second
        print(f" {first} x {second} = {result}")     #math homework
    print("---")
print("math homework done \n")

print(" Task 5: Numbers 0-10 (stopping at 6)")
for num in range(0, 11):
    if num == 6:
        print("ohh! Hit 6 - stopping!")
        break
    print(f"➡ {num}")
print("break time \n")

print(" Task 6: Counting 0-5 (skipping 3)")
for num in range(0, 6):
    if num == 3:
        print(" Skipped 3")
        continue
    print(f" {num}")
print("no 3 allowed \n")

word = input(" Bonus Task: Enter a fun word: ")                   #spelling bee
print(f"Spelling '{word}':")
for letter in word:
    print(f" {letter.upper()}")
print(f"Word spelling  Total letters: {len(word)}")
