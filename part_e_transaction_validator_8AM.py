# ============================================================
# PART E (Bonus): Smart Transaction Validator
# Day 8 Assignment | codewithnavaid
# ============================================================

def get_float_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value = float(input(prompt))
            if min_val is not None and value < min_val:
                print(f"  ⚠ Value must be ≥ {min_val}.")
            elif max_val is not None and value > max_val:
                print(f"  ⚠ Value must be ≤ {max_val}.")
            else:
                return value
        except ValueError:
            print("  ⚠ Please enter a numeric value.")


def get_category_input(prompt):
    valid = ("food", "travel", "electronics", "other")
    while True:
        value = input(prompt).strip().lower()
        if value in valid:
            return value
        print(f"  ⚠ Please enter one of: {', '.join(valid)}.")


def get_int_input(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"  ⚠ Value must be between {min_val} and {max_val}.")
        except ValueError:
            print("  ⚠ Please enter a whole number.")


def get_yes_no_input(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ("yes", "no"):
            return value == "yes"
        print("  ⚠ Please enter 'yes' or 'no'.")


def validate_transaction(amount, category, hour, daily_spent, is_vip):
    """
    Core rule engine for transaction validation.
    Returns (decision, reason) tuple.

    VIP enhancement: doubles all limits via ternary operator.
    """
    # ── VIP Multiplier (ternary operator) ────────────────────
    vip_multiplier = 2 if is_vip else 1

    # ── Dynamic Limits (scaled by VIP status) ────────────────
    single_txn_limit   = 50_000  * vip_multiplier
    daily_limit        = 100_000 * vip_multiplier
    food_limit         = 5_000   * vip_multiplier
    electronics_limit  = 30_000  * vip_multiplier
    # Travel and Other have no specific category cap (only global limits apply)

    # ── Category label for display ───────────────────────────
    vip_tag = " [VIP — 2× limits applied]" if is_vip else ""

    # ════════════════════════════════════════════════════════
    # BLOCKING RULES (highest priority — checked first)
    # ════════════════════════════════════════════════════════

    # TODO 1: Single transaction limit
    if amount > single_txn_limit:
        return (
            "BLOCKED",
            f"Exceeds single transaction limit of ₹{single_txn_limit:,.0f}{vip_tag}."
        )

    # TODO 2: Daily spending limit
    if daily_spent + amount > daily_limit:
        remaining = daily_limit - daily_spent
        return (
            "BLOCKED",
            f"Would exceed daily limit of ₹{daily_limit:,.0f}. "
            f"Remaining allowance: ₹{max(0, remaining):,.0f}{vip_tag}."
        )

    # ════════════════════════════════════════════════════════
    # FLAGGING RULES (checked after blocking rules pass)
    # ════════════════════════════════════════════════════════

    # TODO 3: Unusual hours (before 6 AM or after 11 PM)
    if hour < 6 or hour >= 23:
        return (
            "FLAGGED",
            f"Transaction at {hour:02d}:00 is outside normal hours (06:00–23:00)."
        )

    # TODO 4: Category-specific limits
    if category == "food" and amount > food_limit:
        return (
            "FLAGGED",
            f"Food transaction of ₹{amount:,.0f} exceeds category limit "
            f"of ₹{food_limit:,.0f}{vip_tag}."
        )
    elif category == "electronics" and amount > electronics_limit:
        return (
            "FLAGGED",
            f"Electronics transaction of ₹{amount:,.0f} exceeds category limit "
            f"of ₹{electronics_limit:,.0f}{vip_tag}."
        )

    # ════════════════════════════════════════════════════════
    # TODO 5: All rules passed → APPROVED
    # ════════════════════════════════════════════════════════
    return "APPROVED", f"Transaction within all limits{vip_tag}."


def main():
    print("=" * 60)
    print("   SMART TRANSACTION VALIDATOR — Fraud Detection Engine")
    print("=" * 60)

    # ── Input Collection ─────────────────────────────────────
    amount       = get_float_input("Transaction Amount (₹): ", min_val=0)
    category     = get_category_input("Category (food/travel/electronics/other): ")
    hour         = get_int_input("Hour of Transaction (0–23): ", 0, 23)
    daily_spent  = get_float_input("Amount Already Spent Today (₹): ", min_val=0)
    is_vip       = get_yes_no_input("Is this a VIP account? (yes/no): ")

    # ── Run Rule Engine ──────────────────────────────────────
    decision, reason = validate_transaction(amount, category, hour, daily_spent, is_vip)

    # ── Output ───────────────────────────────────────────────
    print("\n" + "─" * 60)
    print(f"  Transaction  : ₹{amount:,.2f} at {category} shop at {hour:02d}:00")
    print(f"  Daily Spent  : ₹{daily_spent:,.2f}")
    print(f"  VIP Account  : {'Yes' if is_vip else 'No'}")
    print("─" * 60)

    # Decision icon
    icon = {"APPROVED": "✅", "FLAGGED": "⚠️ ", "BLOCKED": "🚫"}.get(decision, "")
    print(f"\n  {icon} DECISION : {decision}")
    print(f"     Reason   : {reason}")
    print("=" * 60)


# ── Demo Run (hardcoded examples from the assignment) ────────
def demo():
    print("\n" + "=" * 60)
    print("   DEMO: Expected Output Verification")
    print("=" * 60)

    test_cases = [
        # (amount, category, hour, daily_spent, is_vip, description)
        (3_000,   "food",        14, 0,       False, "Rs.3000 food at 14:00"),
        (60_000,  "electronics",  2, 0,       False, "Rs.60000 electronics at 02:00"),
        (25_000,  "electronics", 10, 0,       True,  "Rs.25000 electronics, VIP at 10:00"),
        (60_000,  "electronics", 10, 0,       True,  "Rs.60000 electronics, VIP at 10:00"),
        (4_000,   "food",         8, 98_000,  False, "Rs.4000 food, near daily limit"),
    ]

    for amount, category, hour, daily_spent, is_vip, desc in test_cases:
        decision, reason = validate_transaction(amount, category, hour, daily_spent, is_vip)
        icon = {"APPROVED": "✅", "FLAGGED": "⚠️ ", "BLOCKED": "🚫"}.get(decision, "")
        print(f"\n  Transaction: {desc}")
        print(f"  {icon} {decision}: {reason}")

    print()


if __name__ == "__main__":
    demo()          # Show demo output first
    print()
    main()          # Then run interactive mode
