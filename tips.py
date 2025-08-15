from banner import banner_heading
import random

TIPS = (
    "Use a password manager to generate unique, complex passwords.",
    "Enable two-factor authentication (2FA) for all important accounts.",
    "Keep your operating system and applications up to date.",
    "Do not click links or open attachments from unknown sources.",
    "Verify the sender’s email address carefully before responding.",
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

def get_tips(n: int = 3):
    """
    Show cybersecurity tips.
    n: Number of tips to return (1-3).
    """
    # Print a heading for tips section
    banner_heading("Cybersecurity Awareness Tips")

    # Keep n between 1 and 3
    if n < 1:
        n = 1
    elif n > 3:
        n = 3

    # Pick n random tips (no repeats)
    selected_tips = random.sample(TIPS, n)

    # Display each tip in a nice format
    for i, tip in enumerate(selected_tips, start=1):
        print(f"{i}. {tip}\n")

    return selected_tips