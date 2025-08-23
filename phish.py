# phish.py — SafeNet
# ---------------------------------------------------------
# Phishing Email/URL Detector (Pure Python, no regex)
# Detects suspicious patterns in links and emails
# Finds insecure protocols, suspicious keywords, misspelled domains
# Simple rule-based scoring with one main entry function
# ---------------------------------------------------------

from urllib.parse import urlparse
from banner import banner_heading, banner_summary

# ------------------------------
# Lightweight config
# ------------------------------
SUSPICIOUS_KEYWORDS = [
    "urgent", "verify", "account", "update", "click here",
    "password", "bank", "login", "confirm", "limited",
    "security alert", "unusual activity"
]

# Common high-target brands for simple lookalike checks
# We’ll flag domains that *contain* these in altered form (e.g., paypa1, faceb00k)
BRAND_BASE = ["paypal", "google", "microsoft", "apple", "facebook", "amazon", "bank"]

# Simple character swaps often used in lookalikes
LEET_MAP = {
    "0": "o", "1": "l", "3": "e", "4": "a", "5": "s", "7": "t",
    "@": "a", "$": "s", "!": "i"
}


# ------------------------------
# Validation helpers
# ------------------------------
def is_valid_email(text: str) -> bool:
    """
    Very simple email validation:
    - must contain '@' and '.'
    - must not start or end with '@'
    - part before '@' and after '@' must not be empty
    """
    if "@" not in text or "." not in text:
        return False
    if text.startswith("@") or text.endswith("@"):
        return False
    if text.count("@") != 1:
        return False
    local, domain = text.split("@", 1)
    return bool(local) and bool(domain)


def is_valid_url(text: str) -> bool:
    """
    Very simple URL validation:
    - must start with http:// or https://
    - must have at least one '.'
    """
    return (text.startswith("http://") or text.startswith("https://")) and "." in text


def extract_host(text: str) -> str | None:
    """
    Returns the host (domain) from a URL or email.
    """
    if is_valid_url(text):
        return urlparse(text).netloc.lower()    # urlparse(text).netloc → domain with port if any
    elif is_valid_email(text):
        return text.split("@", 1)[-1].lower()   # text.split("@", 1)[-1] → domain part of email
    return None


def registrable_domain(host: str) -> str:
    """
    Gets the base domain (last two parts).
    Example: mail.security.paypal.com -> paypal.com
    """
    parts = host.split(":")[0].split(".")   # remove port if any, then split by '.'
    if len(parts) >= 2:
        return ".".join(parts[-2:]) # last two parts
    return host


def normalize_for_lookalike(s: str) -> str:
    """
    Replace common leetspeak characters with normal ones.
    """
    for k, v in LEET_MAP.items():
        s = s.replace(k, v)
    return s


# ------------------------------
# Core detector
# ------------------------------
def detect_phishing(text: str):
    reasons = []
    score = 0
    raw = text.strip()  # remove leading/trailing spaces
    lower_text = raw.lower()

    is_email = is_valid_email(raw)
    is_url = is_valid_url(raw)

    # Invalid input
    if not (is_email or is_url):
        reasons.append("[!] ALERT: Not a valid email or URL format.")
        score += 30

    # Insecure protocol
    if lower_text.startswith("http://"):
        reasons.append("[-] INSECURE: Uses HTTP instead of HTTPS.")
        score += 25

    # Keyword check
    for kw in SUSPICIOUS_KEYWORDS:
        if kw in lower_text:
            reasons.append(f"[-] INSECURE: Suspicious keyword '{kw}'.")
            score += 8

    # Host checks
    host = extract_host(raw)
    if host:
        reg = registrable_domain(host)

        if host.count(".") >= 4:
            reasons.append("[-] INSECURE: Too many subdomains (fake nesting).")
            score += 12

        # punycode means internationalized domain, xn-- indicates this, internationalized domains means it could be a lookalike domain
        if host.startswith("xn--"):
            reasons.append("[!] ALERT: Internationalized domain (punycode).")
            score += 20

        if sum(ch.isdigit() for ch in host) > 6:
            reasons.append("[-] INSECURE: Too many digits in domain (obfuscation).")
            score += 10

        # Lookalike check
        normalized_host = normalize_for_lookalike(host.replace("-", ""))
        for brand in BRAND_BASE:
            if brand in normalized_host and brand not in host:
                reasons.append(f"[!] ALERT: Domain resembles '{brand}' (lookalike).")
                score += 25
                break

        # Suspicious TLDs
        tld = reg.split(".")[-1]
        if tld in {"xyz", "top", "tk", "icu", "cf", "gq", "ml"}:
            reasons.append(f"[-] INSECURE: Suspicious top-level domain '.{tld}'.")
            score += 12

    # Final verdict
    if score >= 60:
        verdict = "[!] ALERT: HIGH RISK"
    elif score >= 40:
        verdict = "[-] INSECURE: SUSPICIOUS"
    elif score >= 20:
        verdict = "[-] INSECURE: REVIEW ADVISED"
    else:
        verdict = "[+] SAFE"

    # Suggestion
    suggestion = None
    if verdict != "[+] SAFE":
        if is_email:
            suggestion = "  [+] Tip: Verify sender's domain and only trust official addresses."
        elif is_url:
            suggestion = "  [+] Tip: Manually type the official site instead of clicking links."
        else:
            suggestion = "  [+] Tip: Provide a full email (user@domain.tld) or full URL (https://domain.tld)."

    return verdict, score, reasons, suggestion


# ------------------------------
# CLI entry
# ------------------------------
def input_phish():
    banner_heading("Phishing Email/URL Detector")
    user_input = input("Enter an email or URL to check: ").strip()

    verdict, score, reasons, suggestion = detect_phishing(user_input)

    banner_summary("Phishing Analysis")
    print(f"\nResult: {verdict}  (Risk Score: {score})")
    if reasons:
        print("\nFindings:")
        for r in reasons:
            print(f"  {r}")
    if suggestion:
        print(f"\nRecommendation:\n{suggestion}\n")


if __name__ == "__main__":
    input_phish()