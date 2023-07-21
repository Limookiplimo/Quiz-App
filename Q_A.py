import random
from string import ascii_lowercase

import pathlib
try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS_PATH = pathlib.Path(__file__).parent / "quizes.toml"
QUESTIONS = tomllib.loads(QUESTIONS_PATH.read_text())


def run_quiz():
    quizes = prepare_quizes(QUESTIONS_PATH, num_quizes=NUM_QUESTIONS_PER_QUIZ)
    num_correct = 0
    for num, quiz in enumerate(quizes, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_quiz(quiz)

    print(f"Your total score is {num_correct} out of {num} questions.")


def prepare_quizes(path, num_quizes):
    topic_info = tomllib.loads(path.read_text())
    topics = {
        topic["label"]: topic["quizes"] for topic in topic_info.values()
    }
    topic_label = get_ans(
        quiz="Which topic do you want to take?",
        choices=sorted(topics),
    )[0]

    quizes = topics[topic_label]
    num_quizes = min(num_quizes, len(quizes))
    return random.sample(quizes, k=num_quizes)


def get_ans(quiz, choices, num_choices=1, hint=None):
    print(f"{quiz}?")
    labeled_choices = dict(zip(ascii_lowercase, choices))
    if hint:
        labeled_choices["?"] = "Hint"

    for label, choice in labeled_choices.items():
        print(f"{label}){choice}")

    while True:
        # pluralize
        plural_s = " " if num_choices == 1 else f"s (choose {num_choices})"
        ans = input(f"\nchoice{ plural_s}? ")
        answs = set(ans.replace(",", " ").split())

        # Hints
        if hint and "?" in answs:
            print(f"\nHint: {hint}")
            continue

        # invalid answers
        if len(answs) != num_choices:
            plural_s = " " if num_choices == 1 else f"s , separated by comma"  # pluralize
            print(f"Please answer{num_choices}choices{plural_s}")
            continue

        if any((invalid := ans) not in labeled_choices for ans in answs):
            print(
                f"{invalid!r} not a valid choice"
                f"Please use{','.join(labeled_choices)}"
            )
            continue

        return[labeled_choices[ans] for ans in answs]


def ask_quiz(quiz):
    correct_answs = quiz["answs"]
    choices = quiz["answs"] + quiz["choices"]
    ordered_choices = random.sample(choices, k=len(choices))

    answs = get_ans(
        quiz=quiz["quiz"],
        choices=ordered_choices,
        num_choices=len(correct_answs),
        hint=quiz.get("hint"),
    )

    if correct := (set(answs) == set(correct_answs)):
        print("⭐Correct⭐")

    else:
        is_or_are = " is" if len(correct_answs) == 1 else "s are"

        print("\n- ".join([f"No, the answer { is_or_are}: "] + correct_answs))

    if "explanation" in quiz:
        print(f"\nEXPLANATION: \n{quiz['explanation']}")

    return 1 if correct else 0


if __name__ == "__main__":
    run_quiz()
