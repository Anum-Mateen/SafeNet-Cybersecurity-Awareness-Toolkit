# breach.py — SafeNet
# This file checks if a given Email/Username is:
#   → Breached (already leaked / unsafe, shows source + password)
#   → Safe (valid but not found in breach dataset)
#
# Mock Data Breach Checker
# Checks input email/username against mock breached data
# Case-insensitive matching

from data.mock_breached_data import BREACHED_ACCOUNTS
from banner import banner_heading, banner_summary   


# ------------------------------
# Function: is_breached
# ------------------------------
def is_breached(account: str) -> dict | None:
    """
    Check if the input account (email/username) is in the mock breached data.
    Returns:
      Dictionary with breach info → if breached
      None → if not found (safe)
    """
    account_lower = account.lower()

    # STEP 1: Search in BREACHED_ACCOUNTS
    for entry in BREACHED_ACCOUNTS:
        if (
            entry["email"].lower() == account_lower
            or entry["username"].lower() == account_lower
        ):
            return entry    # return the full breach record (email, username, source, password)

    # STEP 2: If not found → Safe
    return None


# ------------------------------
# Wrapper Function for Main
# ------------------------------
def run_breach_checker():
    """
    Runs a simple prompt asking the user for an email/username
    and checks against mock breach data.
    """
    # ✅ Banner heading
    banner_heading("Cybersecurity Breach Checker")

    account = input("Enter your email/username to check: ")

    banner_summary("Breach Check Summary")
    
    result = is_breached(account)
    if result:
        print(f"\n[!] ALERT: {account} was found in a breach!")
        print(f"\t → Email: {result['email']}")
        print(f"\t → Username: {result['username']}")
        print(f"\t → Source: {result['source']}")
        print(f"\t → Password: {result['password']}")
    else:
        print(f"\n[+] SAFE: {account} was NOT found in any breach.")


# ------------------------------
# TESTING (only runs if run directly)
# ------------------------------
if __name__ == "__main__":
    run_breach_checker()