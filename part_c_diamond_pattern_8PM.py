# ============================================================
# PART C: AI-Augmented Task — Diamond Pattern
# Day 8 PM Assignment | codewithnavaid
# ============================================================

# ── EXACT PROMPT USED ────────────────────────────────────────
"""
PROMPT SUBMITTED TO CLAUDE:

You are an expert Python developer. Your task is to write a complete, production-ready Python program that validates Indian PAN (Permanent Account Number) card numbers based on their required format.

Requirements:

Validate the PAN format: 5 uppercase letters, followed by 4 digits, followed by 1 uppercase letter (e.g., ABCDE1234F)
Use if-else conditions for all validation logic (do not use regex or other pattern-matching approaches)
The 4th character of the PAN indicates the taxpayer type—document this in comments but validation of the specific taxpayer type is not required
The program should accept a PAN number as input and return a clear pass/fail validation result
Include error handling for edge cases (None values, non-string inputs, incorrect length, invalid character types)
Provide clear, descriptive output messages indicating what validation rule failed (if applicable)
Include 3-5 test cases demonstrating both valid and invalid PAN numbers
Output: A single, runnable Python script that can be executed immediately without modification. The script should be well-commented and follow PEP 8 style guidelines.
"""

# ── AI-GENERATED CODE ────────────────────────────────────────
def diamond_ai_version(n):
    """AI-generated version — submitted for critique."""
    # Upper half (including middle)
    for i in range(1, n + 1):
        # Print spaces
        for j in range(n - i):
            print(" ", end="")
        # Print asterisks
        for k in range(2 * i - 1):
            print("*", end="")
        print()

    # Lower half
    for i in range(n - 1, 0, -1):
        # Print spaces
        for j in range(n - i):
            print(" ", end="")
        # Print asterisks
        for k in range(2 * i - 1):
            print("*", end="")
        print()


# ── CRITICAL EVALUATION ──────────────────────────────────────
"""
EVALUATION OF AI-GENERATED CODE:

1. Spacing correctness:
   ✅ Correct. Upper half: (n - i) leading spaces, (2i - 1) stars.
      Lower half: (n - i) leading spaces, (2i - 1) stars.
      The math is right — the diamond is symmetric and centred.

2. Readability:
   ⚠ Acceptable but improvable.
     - Variable names i, j, k are generic and non-descriptive.
     - No docstring or inline comments explaining the math.
     - The two halves are near-identical blocks — could be extracted
       into a helper function to avoid repetition (DRY principle).

3. Edge cases (n = 0, n = 1):
   ❌ n = 0: range(1, 1) is empty → prints nothing. No error message.
      A user entering 0 gets silent output — confusing.
   ✅ n = 1: prints a single "*". Correct.
   ❌ Negative n: range(1, -2) is empty → silent. Should be validated.

4. Nested loops vs string tricks:
   ✅ Fully compliant — uses only nested for loops, no string
      multiplication (e.g., no "*" * k or " " * k).

5. Time complexity:
   ⚠ O(n²) — for each of the ~2n rows, we print up to ~2n characters.
      This is the inherent complexity for drawing an n-row diamond.
      The AI didn't mention this — a good answer should note it.
      It cannot be reduced: you must print every character.

SUMMARY:
  The core logic is correct. Main weaknesses:
  - No input validation (n = 0 or negative)
  - Code duplication between upper and lower halves
  - Poor variable naming
  - No complexity analysis
"""

# ── IMPROVED VERSION ─────────────────────────────────────────
def print_row(n_spaces, n_stars):
    """
    Prints one row of the diamond using nested loops only.
    n_spaces: leading spaces before stars
    n_stars : number of asterisks to print
    """
    for _ in range(n_spaces):   # leading spaces
        print(" ", end="")
    for _ in range(n_stars):    # asterisks
        print("*", end="")
    print()                     # newline


def diamond(n):
    """
    Prints a diamond pattern with n rows in the upper half.

    Pattern math:
      Row i (1-indexed from top):
        - Upper half (i = 1..n) : spaces = n-i,  stars = 2i-1
        - Lower half (i = n-1..1): spaces = n-i, stars = 2i-1
      (same formula — just iterates i downward for the lower half)

    Time complexity: O(n²) — inherent cost of printing the shape.
    Space complexity: O(1) — no storage, output only.
    """
    if n <= 0:
        print("  ⚠ Please enter a positive integer (n ≥ 1).")
        return

    # Upper half — i goes 1 → n (growing)
    for i in range(1, n + 1):
        print_row(n_spaces=n - i, n_stars=2 * i - 1)

    # Lower half — i goes n-1 → 1 (shrinking), mirrors upper half
    for i in range(n - 1, 0, -1):
        print_row(n_spaces=n - i, n_stars=2 * i - 1)


def main():
    print("=" * 45)
    print("   DIAMOND PATTERN GENERATOR")
    print("=" * 45)

    # Input validation
    while True:
        try:
            n = int(input("Enter number of rows for upper half: "))
            if n <= 0:
                print("  ⚠ Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("  ⚠ Invalid input. Please enter a whole number.")

    print()
    diamond(n)
    print()

    # Show edge cases
    print("─" * 45)
    print("Edge case n=1:")
    diamond(1)
    print("Edge case n=0:")
    diamond(0)


# ── Demo for submission (no interactive input needed) ────────
if __name__ == "__main__":
    print("AI version (n=4):")
    diamond_ai_version(4)
    print()
    print("Improved version (n=4):")
    diamond(4)
    print()
    print("Improved version (n=6):")
    diamond(6)
    print()
    print("Edge case n=1:")
    diamond(1)
    print()
    print("Edge case n=0:")
    diamond(0)
