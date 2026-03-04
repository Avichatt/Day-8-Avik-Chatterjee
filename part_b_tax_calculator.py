# ============================================================
# PART B: Indian Income Tax Calculator (New Regime FY 2024-25)
# Day 8 Assignment | codewithnavaid
# ============================================================

def calculate_tax(income):
    """
    Applies progressive slab-wise taxation under New Regime FY 2024-25.
    Standard deduction of Rs.75,000 is applied first.
    Returns a tuple: (taxable_income, slab_breakdown, total_tax, effective_rate)
    """
    STANDARD_DEDUCTION = 75_000

    # Tax slabs: (lower_limit, upper_limit, rate_percent)
    slabs = [
        (0,         300_000,   0),
        (300_000,   700_000,   5),
        (700_000,  1_000_000, 10),
        (1_000_000, 1_200_000, 15),
        (1_200_000, 1_500_000, 20),
        (1_500_000, float("inf"), 30),
    ]

    taxable_income = max(0, income - STANDARD_DEDUCTION)
    total_tax = 0
    breakdown = []

    for lower, upper, rate in slabs:
        if taxable_income <= lower:
            break  # Income doesn't reach this slab

        # Amount of income that falls in this slab
        income_in_slab = min(taxable_income, upper) - lower
        tax_in_slab = income_in_slab * rate / 100

        upper_label = f"₹{upper/100_000:.0f}L" if upper != float("inf") else "Above ₹15L"
        breakdown.append({
            "slab": f"₹{lower/100_000:.0f}L – {upper_label}",
            "rate": rate,
            "income_in_slab": income_in_slab,
            "tax": tax_in_slab,
        })
        total_tax += tax_in_slab

    effective_rate = (total_tax / income * 100) if income > 0 else 0
    return taxable_income, breakdown, total_tax, effective_rate


def get_income_input():
    while True:
        try:
            raw = input("Enter Annual Income (₹): ").replace(",", "").strip()
            income = float(raw)
            if income < 0:
                print("  ⚠ Income cannot be negative.")
            else:
                return income
        except ValueError:
            print("  ⚠ Invalid input. Please enter a numeric value.")


def main():
    print("=" * 60)
    print("   INDIAN INCOME TAX CALCULATOR — New Regime FY 2024-25")
    print("=" * 60)

    income = get_income_input()
    taxable_income, breakdown, total_tax, effective_rate = calculate_tax(income)

    print(f"\n{'─' * 60}")
    print(f"  Gross Annual Income   : ₹{income:>14,.2f}")
    print(f"  Standard Deduction    : ₹{75_000:>14,.2f}")
    print(f"  Taxable Income        : ₹{taxable_income:>14,.2f}")
    print(f"{'─' * 60}")
    print(f"  {'Slab':<22} {'Rate':>6}  {'Income in Slab':>16}  {'Tax':>12}")
    print(f"  {'─'*22} {'─'*6}  {'─'*16}  {'─'*12}")

    for row in breakdown:
        print(
            f"  {row['slab']:<22} {row['rate']:>5}%  "
            f"₹{row['income_in_slab']:>14,.2f}  ₹{row['tax']:>11,.2f}"
        )

    print(f"{'─' * 60}")
    print(f"  {'Total Tax Payable':<22}        {'':>16}  ₹{total_tax:>11,.2f}")
    print(f"  Effective Tax Rate    : {effective_rate:.2f}%")
    print(f"  Monthly Tax Liability : ₹{total_tax/12:>12,.2f}")
    print("=" * 60)

    # Nil tax notice
    if total_tax == 0:
        print("  ✅ No tax liability under the New Regime.")
    print()


if __name__ == "__main__":
    main()
