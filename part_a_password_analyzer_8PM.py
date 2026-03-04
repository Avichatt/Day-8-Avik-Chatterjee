# ============================================================
# PART A: Password Strength Analyzer & Generator
# Day 8 PM Assignment | codewithnavaid
# ============================================================

import random
import string


# ── Constants ─────────────────────────────────────────────────
SPECIAL_CHARS = set("!@#$%^&*")

SCORE_RATINGS = [
    (7, "Very Strong", "🟢"),
    (5, "Strong",      "🟡"),
    (3, "Medium",      "🟠"),
    (0, "Weak",        "🔴"),
]


# ── Password Analyzer ─────────────────────────────────────────
def analyze_password(password):
    """
    Evaluates password strength using a for loop over each character.
    Returns (score, max_score, rating, missing_criteria).
    """
    score = 0
    missing = []

    # ── Length scoring ───────────────────────────────────────
    length = len(password)
    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        missing.append("too short (need ≥ 8 chars)")

    # ── Character type checks (using a for loop) ─────────────
    has_upper   = False
    has_lower   = False
    has_digit   = False
    has_special = False

    for ch in password:          # for loop — iterates each character
        if ch.isupper():   has_upper   = True
        if ch.islower():   has_lower   = True
        if ch.isdigit():   has_digit   = True
        if ch in SPECIAL_CHARS: has_special = True

    if has_upper:   score += 1
    else:           missing.append("uppercase letter")

    if has_lower:   score += 1
    else:           missing.append("lowercase letter")

    if has_digit:   score += 1
    else:           missing.append("digit")

    if has_special: score += 1
    else:           missing.append("special character (!@#$%^&*)")

    # ── No more than 2 consecutive repeated characters ───────
    no_triple_repeat = True
    for i in range(len(password) - 2):    # for loop — window of 3
        if password[i] == password[i + 1] == password[i + 2]:
            no_triple_repeat = False
            break

    if no_triple_repeat:
        score += 1
    else:
        missing.append("3+ consecutive identical characters found")

    # ── Determine rating ─────────────────────────────────────
    rating = "Weak"
    icon   = "🔴"
    for min_score, label, emoji in SCORE_RATINGS:
        if score >= min_score:
            rating = label
            icon   = emoji
            break

    return score, 7, rating, icon, missing


# ── Password Generator ────────────────────────────────────────
def generate_password(length):
    """
    Generates a random password of given length using a for loop.
    Guarantees at least one character from each required category.
    """
    if length < 4:
        length = 4  # minimum to satisfy all categories

    char_pool = string.ascii_letters + string.digits + string.punctuation

    # Guarantee at least one from each category
    guaranteed = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*"),
    ]

    # Fill the rest with random choices using a for loop
    rest = []
    for _ in range(length - 4):    # for loop — builds remaining characters
        rest.append(random.choice(char_pool))

    # Shuffle to avoid predictable positions
    all_chars = guaranteed + rest
    random.shuffle(all_chars)

    return "".join(all_chars)


# ── Display Helper ────────────────────────────────────────────
def display_analysis(password, score, max_score, rating, icon, missing, label="Password"):
    print(f"\n  {label}: {password}")
    print(f"  Strength : {score}/{max_score} ({icon} {rating})")
    if missing:
        print(f"  Missing  : {', '.join(missing)}")
    else:
        print("  ✅ All criteria met!")


# ── Main Program ──────────────────────────────────────────────
def main():
    print("=" * 55)
    print("   PASSWORD STRENGTH ANALYZER & GENERATOR")
    print("=" * 55)

    # ── While loop: keep asking until strength ≥ 5 ───────────
    while True:
        password = input("\nEnter password: ").strip()

        if not password:
            print("  ⚠ Password cannot be empty.")
            continue

        score, max_score, rating, icon, missing = analyze_password(password)
        display_analysis(password, score, max_score, rating, icon, missing)

        if score >= 5:
            print("  ✅ Password accepted!")
            break
        else:
            print("  ❌ Too weak. Try again...")

    # ── Password Generator ────────────────────────────────────
    print("\n" + "─" * 55)
    print("  PASSWORD GENERATOR")
    print("─" * 55)

    while True:
        try:
            gen_length = int(input("  Generate a password of length: "))
            if gen_length < 4:
                print("  ⚠ Minimum length is 4.")
            elif gen_length > 128:
                print("  ⚠ Maximum length is 128.")
            else:
                break
        except ValueError:
            print("  ⚠ Please enter a whole number.")

    generated = generate_password(gen_length)
    g_score, g_max, g_rating, g_icon, g_missing = analyze_password(generated)
    display_analysis(generated, g_score, g_max, g_rating, g_icon, g_missing, label="Generated")

    print("=" * 55)


if __name__ == "__main__":
    main()
