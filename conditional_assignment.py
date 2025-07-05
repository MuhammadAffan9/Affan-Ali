print("Hi! I'm BRAINY 1.0 i am here to  play with u")

print("\nHow old are you?") #type your age
age = int(input("Type your age: "))
if age >= 18:
    print("Wow, you're an adult! You can do big things!")
else:                          # tells u about your age
    print("You're a kid like me! Kids are super cool!")

print("\nWhat's your test score?")   #type your score
marks = int(input("Type your score: "))
if marks >= 90:
    print("Grade: A - You're a star!")
elif marks >= 70:
    print("Grade: B - Awesome job!")
elif marks >= 50:                            #tell you about your score
    print("Grade: C - Keep trying!")
else:                                                     
    print("Fail - Don't worry, you'll get it next time!")


print("\nWhat's the weather today?") #type weather
weather = input("Type rainy, sunny, or cloudy: ")
if weather.lower() == "rainy":                        
    print("Grab an umbrella!")
elif weather.lower() == "sunny":
    print("Put on sunglasses!")         #pass comment about weather
elif weather.lower() == "cloudy":
    print("Maybe bring a jacket!")
else:
    print("Stay ready for anything!")


print("\nAre you hungry?")
hungry = input("Type yes or no: ")
if hungry.lower() == "yes":                 #type yes or no and you will get order to eat 
    print("Eat something tasty!")
else:
    print("Snack time later then!")

# Mood chat
print("\nHow do you feel?")
mood = input("Type happy, sad, or bored: ")
if mood.lower() == "happy":                      #type how u feel and you will be preaised by him
    print("Yay, keep shining!")
elif mood.lower() == "sad":
    print("Cheer up soon, okay?")
elif mood.lower() == "bored":
    print("Let’s find fun stuff to do!")
else:
    print("Thanks for telling me!")                #says goof bye

print("\nKhuda hafiz i had fun with u")
