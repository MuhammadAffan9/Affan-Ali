print("Hi! I'm Robo, your fun robot friend. Let's play with choices!")

# Check age
print("\nHow old are you?")
age = int(input("Type your age: "))
if age >= 18:
    print("Wow, you're an adult! You can do big things!")
else:
    print("You're a kid like me! Kids are super cool!")

# Grade a test
print("\nWhat's your test score?")
marks = int(input("Type your score: "))
if marks >= 90:
    print("Grade: A - You're a star!")
elif marks >= 70:
    print("Grade: B - Awesome job!")
elif marks >= 50:
    print("Grade: C - Keep trying!")
else:
    print("Fail - Don't worry, you'll get it next time!")

# Weather tip
print("\nWhat's the weather today?")
weather = input("Type rainy, sunny, or cloudy: ")
if weather.lower() == "rainy":
    print("Grab an umbrella!")
elif weather.lower() == "sunny":
    print("Put on sunglasses!")
elif weather.lower() == "cloudy":
    print("Maybe bring a jacket!")
else:
    print("Stay ready for anything!")

# Hungry check
print("\nAre you hungry?")
hungry = input("Type yes or no: ")
if hungry.lower() == "yes":
    print("Eat something tasty!")
else:
    print("Snack time later then!")

# Mood chat
print("\nHow do you feel?")
mood = input("Type happy, sad, or bored: ")
if mood.lower() == "happy":
    print("Yay, keep shining!")
elif mood.lower() == "sad":
    print("Cheer up soon, okay?")
elif mood.lower() == "bored":
    print("Let’s find fun stuff to do!")
else:
    print("Thanks for telling me!")

print("\nBye-bye! Robo had fun with you!")