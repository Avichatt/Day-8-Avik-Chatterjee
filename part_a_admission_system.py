# ============================================================
# PART A: Student Admission Decision System
# Day 8 Assignment | codewithnavaid
# ============================================================

def get_float_input(prompt, min_val, max_val):
    """Validate and return a float input within a given range."""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"  ⚠ Please enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("  ⚠ Invalid input. Please enter a numeric value.")


def get_yes_no_input(prompt):
    """Validate and return a yes/no input."""
    while True:
        value = input(prompt).strip().lower()
        if value in ("yes", "no"):
            return value
        print("  ⚠ Please enter 'yes' or 'no'.")


def get_category_input(prompt):
    """Validate and return a valid category input."""
    valid = ("general", "obc", "sc_st")
    while True:
        value = input(prompt).strip().lower()
        if value in valid:
            return value
        print(f"  ⚠ Please enter one of: {', '.join(valid)}.")


def evaluate_admission():
    print("=" * 55)
    print("   UNIVERSITY ADMISSION SCREENING SYSTEM")
    print("=" * 55)

    # ── Input Collection (with validation) ──────────────────
    entrance_score      = get_float_input("Entrance Score (0–100): ", 0, 100)
    gpa                 = get_float_input("GPA (0–10): ",             0, 10)
    has_recommendation  = get_yes_no_input("Recommendation Letter (yes/no): ")
    category            = get_category_input("Category (general/obc/sc_st): ")
    extracurricular     = get_float_input("Extracurricular Score (0–10): ", 0, 10)

    # ── Category-wise cutoffs ────────────────────────────────
    cutoffs = {"general": 75, "obc": 65, "sc_st": 55}
    min_score = cutoffs[category]

    # ── Bonus Calculation ────────────────────────────────────
    bonus = 0
    bonus_details = []

    if has_recommendation == "yes":
        bonus += 5
        bonus_details.append("+5 (recommendation)")

    if extracurricular > 8:
        bonus += 3
        bonus_details.append("+3 (extracurricular)")

    effective_score = entrance_score + bonus

    # ── Display Bonus Summary ────────────────────────────────
    print("\n" + "-" * 55)
    if bonus_details:
        print(f"Bonus Applied  : {' '.join(bonus_details)}")
    else:
        print("Bonus Applied  : None")
    print(f"Effective Score: {effective_score:.1f}")
    print("-" * 55)

    # ── Admission Logic ──────────────────────────────────────
    print("\nResult:")

    # Rule 1: Auto-admit with scholarship (highest priority)
    if entrance_score >= 95:
        print("✅ ADMITTED (Scholarship)")
        print(f"Reason: Entrance score ≥ 95 — automatic scholarship admission.")

    # Rule 2: Check GPA first (universal requirement)
    elif gpa < 7.0:
        print("❌ REJECTED")
        print(f"Reason: GPA {gpa} is below the minimum requirement of 7.0.")

    # Rule 3: Meets both score and GPA cutoff → Regular admit
    elif effective_score >= min_score:
        print("✅ ADMITTED (Regular)")
        category_label = category.upper().replace("_", "/")
        print(
            f"Reason: Meets {category_label} cutoff "
            f"({effective_score:.1f} ≥ {min_score}) "
            f"and GPA requirement ({gpa} ≥ 7.0)."
        )

    # Rule 4: Within 5 points of cutoff → Waitlisted
    elif effective_score >= min_score - 5:
        print("⏳ WAITLISTED")
        print(
            f"Reason: Effective score {effective_score:.1f} is close to the "
            f"{category.upper()} cutoff of {min_score}, but does not meet it."
        )

    # Rule 5: Too far below cutoff → Rejected
    else:
        shortfall = min_score - effective_score
        print("❌ REJECTED")
        print(
            f"Reason: Effective score {effective_score:.1f} is {shortfall:.1f} points "
            f"below the {category.upper()} cutoff of {min_score}."
        )

    print("=" * 55)


# ── Entry Point ──────────────────────────────────────────────
if __name__ == "__main__":
    evaluate_admission()
