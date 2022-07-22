import random
from string import ascii_lowercase

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS = {
    "When was the first known use of the word 'quiz'": [
        "1781", "1771", "1871", "1881"
    ],
    "Which built-in function can get information from the user": [
        "input", "get", "print", "write"
    ],
    "Which keyword do you use to loop over a given list of elements": [
        "for", "while", "each", "loop"
    ],
    "What's the purpose of the built-in zip() function": [
        "To iterate over two or more sequences at the same time",
        "To combine several strings into one",
        "To compress several files into one archive",
        "To get information from the user",
    ],
    "What's the name of Python's sorting algorithm": [
        "Timsort", "Quicksort", "Merge sort", "Bubble sort"
    ],
}

num_quiz = min(NUM_QUESTIONS_PER_QUIZ, len(QUESTIONS))
quizes = random.sample(list(QUESTIONS.items()), k=num_quiz)

num_correct = 0
for num, (quiz, choices) in enumerate(quizes, start=1):
    print(f"\nQUESTION {num}: ")
    print(f"{quiz}?")
    correct_ans = choices[0]
    labeled_choices = dict(
        zip(ascii_lowercase, random.sample(choices, k=len(choices))))

    for label, choice in labeled_choices.items():
        print(f"{label}) {choice}")

    while (ans_label := input("\nYour choice? ")) not in labeled_choices:
        print(f"Please pick either: {','.join(labeled_choices)}")

    answer = labeled_choices[ans_label]
    if answer == correct_ans:
        num_correct += 1
        print("⭐Correct⭐")
    else:
        print(f"The answer is {correct_ans!r}, not {answer!r}")
    print(f"Your current score is {num_correct} out of {num}")
print(f"Your total score is {num_correct} out of {num}")
