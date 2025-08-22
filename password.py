# password.py — SafeNet
# ---------------------------------------------------------
# Password Strength Checker
# Evaluates length, character variety, and complexity
# Provides actionable improvement suggestions
# ---------------------------------------------------------

from banner import banner_heading, banner_summary
import random


# ------------------------------
# Function: check_password
# ------------------------------
def check_password(password: str) -> tuple[str, list[str]]:
    """
    Checks the strength of a password.
    Returns:
      (strength_label: 'Strong' | 'Medium' | 'Weak', reasons: list[str])
    """
    reasons = []
    score = 0  # points for each rule passed

    # Rule 1: length
    if len(password) >= 8:
        score += 1
    else:
        reasons.append("[!] Too short: use at least 8 characters.")

    # Rule 2: contains number
    if any(ch.isdigit() for ch in password):
        score += 1
    else:
        reasons.append("[!] Add at least one number (0-9).")

    # Rule 3: contains uppercase
    if any(ch.isupper() for ch in password):
        score += 1
    else:
        reasons.append("[!] Add at least one uppercase letter (A-Z).")

    # Rule 4: contains lowercase
    if any(ch.islower() for ch in password):
        score += 1
    else:
        reasons.append("[!] Add at least one lowercase letter (a-z).")

    # Rule 5: contains special character
    specials = "~`!@#$%^&*()-_=+[]{}|;:'\",.<>?/"
    if any(ch in specials for ch in password):
        score += 1
    else:
        reasons.append("[!] Add at least one special character like @ # $ !")

    # Determine label
    if score == 5:
        label = "[+] Strong"
    elif score >= 3:
        label = "[!] Medium"
    else:
        label = "[!] Weak"

    return label, reasons

# ------------------------------
# Function: suggest_password
# ------------------------------
def suggest_password() -> str:
    """
    Suggests an ultra-random but easy-to-understand password.
    Combines multiple readable words, random capitalization,
    symbols, and numbers.
    Example: Luna#CYPher94!Mint
    """

    # --------------------------
    # Inner function: random_case
    # --------------------------
    def random_case(word: str) -> str:
        """
        Randomly changes some letters in the word to uppercase or lowercase.
        Example: "Wolf" -> "wOlF" or "WOLF"
        """
        new_word = ""
        for c in word:
            if random.choice([True, False]):
                new_word += c.upper()
            else:
                new_word += c.lower()
        return new_word

    # List of words and symbols to choose from
    words = ["Sky", "Mint", "Wolf", "Nova", "Luna", "Aqua", 
             "Pixel", "Greet", "Cloud", "Cipher", "Zen", "Echo", 
             "Storm", "Glide", "Frost", "Wave"]

    specials = ["@", "#", "$", "!", "%", "&", "*"]

    # STEP 1: Pick 3 random words (all different)
    chosen_words = random.sample(words, 3)

    # STEP 2: Apply random_case to each word
    changed_words = []
    for w in chosen_words:
        changed_words.append(random_case(w))

    # STEP 3: Pick one random special character
    sp = random.choice(specials)

    # STEP 4: Pick a random number (10–9999)
    num = str(random.randint(10, 9999))

    # STEP 5: Combine everything
    parts = changed_words + [sp, num]

    # STEP 6: Shuffle order
    random.shuffle(parts)

    # STEP 7: Join into one string
    password = "".join(parts)

    return password


# ------------------------------
# Wrapper for running directly
# ------------------------------
def run_password_checker():
    banner_heading("Password Strength Checker")

    password = input("Enter a password to evaluate: ")

    strength, feedback = check_password(password)

    banner_summary("Password Analysis")

    print(f"\nResult: {strength}")
    if feedback:
        print("\nRecommendations:")
        for reason in feedback:
            print(f"  - {reason}")
        print(f"\nSuggested Strong Password Example: {suggest_password()}")
    else:
        print("\n[+] Your password meets all recommended security standards.")
        print(f"[Optional] Even stronger example: {suggest_password()}")


# ------------------------------
# Run if executed directly
# ------------------------------
if __name__ == "__main__":
    run_password_checker()