# ============================================================
# PART D (Bonus): Daily Transaction Analyzer — Paytm Case Study
# Day 8 PM Assignment | codewithnavaid
# ============================================================

# ── Data Storage ─────────────────────────────────────────────
transactions = []          # list of dicts: {amount, type, category, high_value}
category_totals = {}       # bonus: spending breakdown by category

# ── Valid inputs ──────────────────────────────────────────────
VALID_TYPES      = ("credit", "debit")
VALID_CATEGORIES = ("food", "travel", "bills", "shopping", "other")
HIGH_VALUE_LIMIT = 10_000


def get_transaction_input():
    """Collect and validate one transaction from the user."""
    # Amount
    while True:
        try:
            amount = float(input("  Amount (₹): "))
            if amount <= 0:
                print("    ⚠ Amount must be positive.")
            else:
                break
        except ValueError:
            print("    ⚠ Please enter a numeric value.")

    # Type
    while True:
        txn_type = input("  Type (credit/debit): ").strip().lower()
        if txn_type in VALID_TYPES:
            break
        print(f"    ⚠ Enter one of: {', '.join(VALID_TYPES)}.")

    # Category (bonus enhancement)
    while True:
        category = input(f"  Category ({'/'.join(VALID_CATEGORIES)}): ").strip().lower()
        if category in VALID_CATEGORIES:
            break
        print(f"    ⚠ Enter one of: {', '.join(VALID_CATEGORIES)}.")

    return amount, txn_type, category


def print_bar_chart(txn_list):
    """
    Prints a bar chart of the last (up to) 10 transactions.
    Each ₹1000 (or part thereof) is represented by one *.
    Uses a for loop with enumerate.
    """
    last_10 = txn_list[-10:]   # slice last 10
    print("\n  📊 Bar Chart — Last 10 Transactions (★ = ₹1,000)")
    print("  " + "─" * 48)

    for idx, txn in enumerate(last_10, start=1):    # for loop with enumerate
        bars = max(1, int(txn["amount"] / 1_000))   # at least 1 bar visible
        bar_str = ""
        for _ in range(bars):                        # for loop — build bar
            bar_str += "★"

        flag     = " 🚨 HIGH VALUE" if txn["high_value"] else ""
        txn_icon = "⬆" if txn["type"] == "credit" else "⬇"
        print(
            f"  {idx:>2}. {txn_icon} ₹{txn['amount']:>9,.0f}  "
            f"[{txn['category']:<8}]  {bar_str}{flag}"
        )


def print_category_breakdown(cat_totals):
    """Bonus: show spending breakdown per category."""
    if not cat_totals:
        return
    print("\n  🗂  Spending Breakdown by Category")
    print("  " + "─" * 36)
    total_spent = sum(cat_totals.values())
    for cat, amount in sorted(cat_totals.items(), key=lambda x: -x[1]):
        pct = (amount / total_spent * 100) if total_spent else 0
        print(f"  {cat:<10}: ₹{amount:>10,.2f}  ({pct:.1f}%)")


def print_summary(txn_list):
    """Calculates and prints the full analytics summary."""
    if not txn_list:
        print("  No transactions recorded.")
        return

    total_credit = sum(t["amount"] for t in txn_list if t["type"] == "credit")
    total_debit  = sum(t["amount"] for t in txn_list if t["type"] == "debit")
    net_balance  = total_credit - total_debit
    count        = len(txn_list)
    highest      = max(t["amount"] for t in txn_list)
    average      = sum(t["amount"] for t in txn_list) / count
    high_value_count = sum(1 for t in txn_list if t["high_value"])

    print("\n  📋 TRANSACTION SUMMARY")
    print("  " + "═" * 40)
    print(f"  Total Transactions  : {count}")
    print(f"  Total Credits   (⬆) : ₹{total_credit:>12,.2f}")
    print(f"  Total Debits    (⬇) : ₹{total_debit:>12,.2f}")
    print(f"  Net Balance         : ₹{net_balance:>12,.2f}  {'✅' if net_balance >= 0 else '⚠'}")
    print(f"  Highest Transaction : ₹{highest:>12,.2f}")
    print(f"  Average Transaction : ₹{average:>12,.2f}")
    print(f"  High-Value Txns 🚨  : {high_value_count}")
    print("  " + "═" * 40)


def main():
    print("=" * 55)
    print("   PAYTM MINI ANALYTICS DASHBOARD")
    print("=" * 55)
    print("  Enter transactions one by one.")
    print("  Type 'done' when finished.\n")

    # TODO 1 & 2: While loop — accept transactions until 'done'
    while True:
        print("─" * 35)
        cmd = input("  Press Enter for new transaction (or type 'done'): ").strip().lower()

        if cmd == "done":
            break

        amount, txn_type, category = get_transaction_input()

        # TODO 3: Flag high-value transactions
        is_high_value = amount > HIGH_VALUE_LIMIT
        if is_high_value:
            print(f"  🚨 HIGH VALUE transaction flagged! (> ₹{HIGH_VALUE_LIMIT:,})")

        # TODO 2: Store transaction
        transactions.append({
            "amount":     amount,
            "type":       txn_type,
            "category":   category,
            "high_value": is_high_value,
        })

        # Bonus: update category totals (only track debits as spending)
        if txn_type == "debit":
            category_totals[category] = category_totals.get(category, 0) + amount

        print(f"  ✅ Recorded: {txn_type.upper()} ₹{amount:,.2f} [{category}]")

    if not transactions:
        print("\n  No transactions entered. Exiting.")
        return

    # TODO 5: Bar chart of last 10
    print_bar_chart(transactions)

    # Bonus: category breakdown
    print_category_breakdown(category_totals)

    # TODO 4 & 6: Summary stats
    print_summary(transactions)


# ── Demo mode (for testing without interactive input) ────────
def demo():
    """Runs a hardcoded demo to show all features."""
    demo_data = [
        (3_000,  "debit",  "food"),
        (50_000, "credit", "other"),
        (15_000, "debit",  "shopping"),   # high value
        (800,    "debit",  "food"),
        (12_000, "credit", "other"),
        (2_500,  "debit",  "bills"),
        (75_000, "debit",  "travel"),     # high value
        (500,    "debit",  "food"),
        (4_200,  "debit",  "shopping"),
        (1_100,  "debit",  "bills"),
        (8_900,  "credit", "other"),
        (300,    "debit",  "food"),
    ]

    demo_txns = []
    demo_cats = {}

    for amount, txn_type, category in demo_data:
        is_hv = amount > HIGH_VALUE_LIMIT
        demo_txns.append({"amount": amount, "type": txn_type,
                           "category": category, "high_value": is_hv})
        if txn_type == "debit":
            demo_cats[category] = demo_cats.get(category, 0) + amount

    print("=" * 55)
    print("   DEMO: PAYTM ANALYTICS DASHBOARD")
    print("=" * 55)
    print_bar_chart(demo_txns)
    print_category_breakdown(demo_cats)

    # Swap globals for demo
    global transactions, category_totals
    transactions   = demo_txns
    category_totals = demo_cats
    print_summary(demo_txns)


if __name__ == "__main__":
    demo()
