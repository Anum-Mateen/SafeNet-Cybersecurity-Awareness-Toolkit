# main.py — SafeNet
# ---------------------------------------------------------
# Entry point for Cybersecurity Awareness Toolkit
# Provides menu-driven CLI for all modules
# ---------------------------------------------------------

from banner import banner_main, banner_heading, banner_menu
from quiz import start_quiz
from tips import get_tips
from breach import run_breach_checker
from password import run_password_checker
from phish import input_phish
import stats as s

# ------------------------------
# Menu
# ------------------------------
def main():
    banner_main()
    banner_heading("WELCOME TO SafeNet")
    username = input("Enter your username: ").strip()
    s.ensure_user(username)

    while True:
        banner_menu()
        print("\t1. Take Cybersecurity Quiz")
        print("\t2. Check Email/Link for Phishing")
        print("\t3. Test Your Password Strength")
        print("\t4. Get Cybersecurity Tips")
        print("\t5. Data Breach Simulator")
        print("\t6. View My Statistics")
        print("\t7. Leaderboard Performers")
        print("\t8. Exit")
        print("\n")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            level, score = start_quiz()
            s.add_quiz_score(username, level, score)
        elif choice == "2":
            found_suspicious = input_phish()
            s.record_phishing_check(username, found_suspicious)
        elif choice == "3":
            run_password_checker()
            s.record_password_check(username)
        elif choice == "4":
            get_tips()
        elif choice == "5":
            run_breach_checker()
            s.record_breach_check(username)
        elif choice == "6":
            s.display_user_stats(username)
        elif choice == "7":
            s.display_leaderboard()
        elif choice == "8":
            banner_heading("EXITING SafeNet!")
            print("\nGoodbye! Stay safe online.")
            print("\n\n" + "=" * 70)
            break
        else:
            print("Invalid choice. Please try again.")


# ------------------------------
# Runner
# ------------------------------
if __name__ == "__main__":
    main()