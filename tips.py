# tips.py — SafeNet
# ---------------------------------------------------------
# Cybersecurity Tips Generator
# Stores 30+ immutable tips and provides random selection
# 1–3 tips per request
# ---------------------------------------------------------

from banner import banner_heading, banner_summary
import random

# ------------------------------
# Immutable cybersecurity tips
# ------------------------------
TIPS = (
    "Use a password manager to generate unique, complex passwords.",
    "Enable two-factor authentication (2FA) for all important accounts.",
    "Keep your operating system and applications up to date.",
    "Do not click links or open attachments from unknown sources.",
    "Verify the sender's email address carefully before responding.",
    "Ensure websites use HTTPS before entering sensitive information.",
    "Back up important files to secure, offline storage regularly.",
    "Lock your computer and phone when not in use.",
    "Never reuse passwords across multiple accounts.",
    "Use a VPN when browsing on public Wi-Fi.",
    "Review and limit app permissions on your devices.",
    "Be cautious of emails with urgent or threatening language.",
    "Check URLs for misspellings or suspicious domain names.",
    "Update your router firmware and change default credentials.",
    "Use long passphrases instead of short passwords.",
    "Be cautious when scanning QR codes from unknown sources.",
    "Disable macros in Microsoft Office documents by default.",
    "Log out from accounts when using shared or public computers.",
    "Monitor your accounts for unusual login activity.",
    "Limit personal details shared on social media.",
    "Report suspicious emails, messages, or calls to IT/security.",
    "Use antivirus software and keep it updated.",
    "Cover your webcam when not in use to prevent spying.",
    "Avoid downloading software from unofficial websites.",
    "Use encryption for sensitive files and communications.",
    "Be wary of free USB drives or unknown charging stations.",
    "Set strong, unique PIN codes for devices and SIM cards.",
    "Clear browsing history and cookies on shared devices.",
    "Check privacy settings on social media accounts regularly.",
    "Shred or securely dispose of documents with personal data.",
)

# ---------------------------------
# Helper: Get valid number of tips
# ---------------------------------
def get_num_tips() -> int:
    """Ask user how many tips they want and ensure it's within 1-3."""
    try:
        num = int(input("How many tips would you like (1-3)? ").strip())
    except ValueError:
        num = 3  # Default if invalid
    return max(1, min(3, num))  # Clamp between 1 and 3

# ------------------------------
# Function: get_tips
# ------------------------------
def get_tips() -> list[str]:
    """
    Display random cybersecurity tips.
    Returns:
        List of selected tips.
    """

    # Show banner heading
    banner_heading("Cybersecurity Awareness Tips")

    # Ask once, no repeated logic
    num_tips = get_num_tips()

    # Randomly pick tips without repeats
    selected_tips = random.sample(TIPS, num_tips)

    # Display tips
    banner_summary("Your Cybersecurity Tips")
    for idx, tip in enumerate(selected_tips, start=1):
        print(f"\n  {idx}. {tip}")
    
    print()
    return selected_tips

# ------------------------------
# Run tips generator directly
# ------------------------------
if __name__ == "__main__":
    get_tips()