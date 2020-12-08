# quiz.py

correct_answer_count = 0

# First Question
answer = int(input("What's 1 + 1? "))

if answer == 2:
    print("You're correct!")
    correct_answer_count += 1

if correct_answer_count > 1:
    print(f"You got {correct_answer_count} questions right!")
else:
    print(f"You got {correct_answer_count} question right!")