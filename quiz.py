# quiz.py — SafeNet
# ---------------------------------------------------------
# Multi-level Cybersecurity Quiz
# Beginner, Intermediate, Advanced
# Randomized questions with no repeats per session
# Provides engaging feedback based on performance
# ---------------------------------------------------------

from data.quiz_questions import questions
from banner import banner_heading, banner_summary
import random

# ------------------------------
# Function: get_valid_input
# ------------------------------
def get_valid_input(prompt: str, choices: list[str]) -> str:
    """
    Keep prompting until user enters a valid choice.
    Returns the valid input.
    """
    while True:
        choice = input(prompt).strip()
        if choice in choices:
            return choice
        print(f"[!] Invalid choice! Please enter one of: {', '.join(choices)}")

# ------------------------------
# Function: load_quiz_questions
# ------------------------------
def load_quiz_questions(level: str) -> list[dict]:
    """
    Filter all questions from data based on difficulty level.
    Returns a list of questions.
    """
    return [q for q in questions if q["level"] == level]

# ------------------------------
# Function: ask_questions
# ------------------------------
def ask_questions(questions_list: list[dict], num_questions: int = 5) -> tuple[int, int]:
    """
    Ask the user questions and track score.
    Randomizes questions and ensures no repeats.
    Returns score and total questions asked.
    """
    score = 0
    random.shuffle(questions_list)
    selected_questions = questions_list[:num_questions]

    for idx, q in enumerate(selected_questions, start=1):
        print(f"\n--- Question {idx} ---")
        print(q['q'])
        for key, value in q['options'].items():
            print(f"    {key}: {value}")

        answer = get_valid_input("Your answer (a/b/c/d): ", ["a", "b", "c", "d"])

        if answer == q['answer']:
            print("[+] Correct!")
            score += 1
        else:
            print(f"[!] Wrong! The correct answer was {q['answer']}.")
            print(f"    Explanation: {q['explain']}")

    return score, len(selected_questions)

# ------------------------------
# Function: quiz_feedback
# ------------------------------
def quiz_feedback(score: int, total: int) -> str:
    """
    Provides creative feedback based on score.
    🔒 Performance Levels:
    - Very Strong → [Cyber Guardian]
    - Strong → [Cyber Defender]
    - Medium → [Cyber Apprentice]
    - Weak → [Cyber Novice]
    """
    if score == total:
        return "\n[Cyber Guardian] Excellent! You mastered this level.\n"
    elif score >= total - 1:
        return "\n[Cyber Defender] Great work! A bit more practice to reach mastery.\n"
    elif score >= total // 2:
        return "\n[Cyber Apprentice] Good start, but some concepts need review.\n"
    else:
        return "\n[Cyber Novice] Keep learning! Strengthen your cybersecurity knowledge.\n"

# ------------------------------
# Function: start_quiz
# ------------------------------
def start_quiz():
    """
    Main entry point to start the quiz.
    Shows banners, asks difficulty level, runs questions, and shows feedback.
    """
    banner_heading("Cybersecurity Awareness Quiz")

    print("Select Difficulty Level:")
    print("1) Beginner\n2) Intermediate\n3) Advanced")

    level_map = {"1": "beginner", "2": "intermediate", "3": "advanced"}
    level_choice = get_valid_input("Enter your choice (1/2/3): ", ["1", "2", "3"])
    level = level_map[level_choice]

    questions_list = load_quiz_questions(level)
    if not questions_list:
        print("[!] No questions available for this level.")
        return

    score, total = ask_questions(questions_list, num_questions=5)

    banner_summary("Quiz Summary")
    print(f"\nScore: {score}/{total}")
    percentage = (score / total) * 100
    print(f"Percentage: {percentage:.2f}%")
    print(f"{quiz_feedback(score, total)}\n")
    return level, percentage

# ------------------------------
# Run if executed directly
# ------------------------------
if __name__ == "__main__":
    result = start_quiz()