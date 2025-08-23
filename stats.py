# stats.py — SafeNet
# ---------------------------------------------------------
# Tracks user statistics for learning & awareness
# Works entirely in Python (no JSON storage used here)
# Handles multiple users, feature progress, and leaderboard
# Stores records in data/leaderboard_data.py (Python dict)
# ---------------------------------------------------------

from datetime import datetime
import importlib
import data.leaderboard_data as db   # storage file
from banner import banner_heading, banner_summary

# ------------------------------
# Global in-memory storage
# ------------------------------
# Structure:
# {
#   "username": {
#       "quiz_scores": [80, 90, 100],
#       "phishing_checks": 3,
#       "suspicious_found": 1,
#       "password_checks": 2,
#       "breach_checks": 1,
#       "last_active": "2025-08-23 14:30"
#   },
#   ...
# }

USER_STATS = {}

# ------------------------------
# User management
# ------------------------------
def ensure_user(username: str):
    """Ensure a user record exists in storage with level-wise quiz tracking."""
    if username not in db.USER_STATS:
        db.USER_STATS[username] = {
            "quiz_scores": {
                "beginner": [],
                "intermediate": [],
                "advanced": []
            },
            "phishing_checks": 0,
            "suspicious_found": 0,
            "password_checks": 0,
            "breach_checks": 0,
            "last_active": None
        }
    db.USER_STATS[username]["last_active"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save()

# ------------------------------
# Save & Reload
# ------------------------------
def save():
    """Write updated USER_STATS back to leaderboard_data.py"""
    with open("data/leaderboard_data.py", "w", encoding="utf-8") as f:
        f.write("# Auto-generated user stats — SafeNet\n")
        f.write("USER_STATS = " + repr(db.USER_STATS) + "\n")

def reload():
    """Reload updated data (in case of external changes)."""
    importlib.reload(db)


# ------------------------------
# Update functions
# ------------------------------
def add_quiz_score(username: str, level: str, score: int):
    """Store a quiz score for a user at a specific level."""
    ensure_user(username)
    if level not in db.USER_STATS[username]["quiz_scores"]:
        db.USER_STATS[username]["quiz_scores"][level] = []
    db.USER_STATS[username]["quiz_scores"][level].append(score)
    save()

def record_phishing_check(username: str, suspicious: bool):
    """Track phishing checks and suspicious detections."""
    ensure_user(username)
    db.USER_STATS[username]["phishing_checks"] += 1
    if suspicious:
        db.USER_STATS[username]["suspicious_found"] += 1
    save()


def record_password_check(username: str):
    """Track password strength checks performed by the user."""
    ensure_user(username)
    db.USER_STATS[username]["password_checks"] += 1
    save()


def record_breach_check(username: str):
    """Track data breach lookups by the user."""
    ensure_user(username)
    db.USER_STATS[username]["breach_checks"] += 1
    save()


# ------------------------------
# Display functions
# ------------------------------
def display_user_stats(username: str):
    """Pretty print user’s progress and awareness stats."""
    if username not in db.USER_STATS:
        print(f"[!] No stats found for user '{username}'.")
        return

    stats = db.USER_STATS[username]
    banner_heading(f"User Stats — {username}")

    print(f"- Last Active: {stats['last_active']}")
    
    print("- Quiz Attempts:")
    for level, scores in stats["quiz_scores"].items():
        print(f"  > {level.capitalize()}: {len(scores)} attempts")
        if scores:
            print(f"    > Best Score: {max(scores)}")
            print(f"    > All Scores: {scores}")

    print(f"- Phishing Checks: {stats['phishing_checks']} (Suspicious Found: {stats['suspicious_found']})")
    print(f"- Password Checks: {stats['password_checks']}")
    print(f"- Breach Checks: {stats['breach_checks']}")


def get_level_leaderboard(level: str):
    """Return leaderboard for a specific quiz level."""
    leaderboard = []
    for user, stats in db.USER_STATS.items():
        scores = stats["quiz_scores"].get(level, [])
        best = max(scores) if scores else 0
        leaderboard.append((user, best))
    leaderboard.sort(key=lambda x: x[1], reverse=True)
    return leaderboard


def display_leaderboard():
    """Print the leaderboard level-wise to the CLI."""
    banner_heading("🏆 Leaderboard — Level-wise Performance")

    for level in ["beginner", "intermediate", "advanced"]:
        banner_summary(f"Level: {level.capitalize()}")
        print()
        leaderboard = get_level_leaderboard(level)
        if all(score == 0 for _, score in leaderboard):
            print(" No attempts yet.")
        else:
            for rank, (user, score) in enumerate(leaderboard, start=1):
                if score > 0:
                    print(f" {rank}. {user} — {score} pts")
    print()


# ------------------------------
# Main runner (demo only)
# ------------------------------
def main():
    add_quiz_score("Anum", "beginner", 85)
    add_quiz_score("Anum", "beginner", 95)
    add_quiz_score("Anum", "intermediate", 70)

    add_quiz_score("Muqaddas", "advanced", 90)
    add_quiz_score("Muqaddas", "beginner", 60)

    record_phishing_check("Anum", suspicious=True)
    record_password_check("Anum")
    record_breach_check("Anum")

    display_user_stats("Anum")
    display_user_stats("Muqaddas")
    display_leaderboard()


if __name__ == "__main__":
    main()