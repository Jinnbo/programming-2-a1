# quiz.py

answers_correct = 0

# Ask a question
print("Who is the coolest teacher in the world?")

# Get their answer
answer = input().lower().strip("!,.? ")

# See if they're right
if answer in ["mr. allan", "bill nye"]:
    print("You got it right!")
    answers_correct += 1
else:
    print("Sorry, not sorry. It's either Mr. Allan or Bill Nye.")

if answers_correct != 1:
    print(f"You got {answers_correct} answers correct!")
else:
    print(f"You got {answers_correct} answer correct!")