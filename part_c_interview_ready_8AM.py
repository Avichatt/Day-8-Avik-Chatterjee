# ============================================================
# PART C: Interview Ready
# Day 8 Assignment | codewithnavaid
# ============================================================

# ─────────────────────────────────────────────────────────────
# Q1: elif vs multiple if statements
# ─────────────────────────────────────────────────────────────
"""
CONCEPTUAL ANSWER
─────────────────
elif (else-if):
  - Creates a MUTUALLY EXCLUSIVE chain. Once one condition is True,
    the rest are skipped entirely.
  - Only ONE branch can execute per run.

Multiple if:
  - Each `if` is evaluated INDEPENDENTLY, regardless of whether
    a previous `if` was True.
  - MULTIPLE branches can execute in the same run.

Example where they produce different output:
────────────────────────────────────────────
Input: score = 85

--- Using multiple if ---
if score >= 60: grade = 'D'   # True  → grade = 'D'
if score >= 70: grade = 'C'   # True  → grade = 'C'  (overwrites)
if score >= 80: grade = 'B'   # True  → grade = 'B'  (overwrites)
if score >= 90: grade = 'A'   # False → skipped
Output: grade = 'B'  ✅ (happens to be correct here, but logic is wrong)

--- Using elif ---
if score >= 90:   grade = 'A'  # False → skipped
elif score >= 80: grade = 'B'  # True  → grade = 'B', rest skipped
elif score >= 70: grade = 'C'  # skipped
elif score >= 60: grade = 'D'  # skipped
Output: grade = 'B'  ✅

BUT watch what happens at score = 95 with a MODIFIED multiple-if:

if score >= 60: print("Pass")      # True  → prints "Pass"
if score >= 90: print("Excellent") # True  → prints "Excellent"

Output (multiple if): "Pass" AND "Excellent" — TWO lines printed.

With elif:
if score >= 90:   print("Excellent")  # True  → prints "Excellent", stops.
elif score >= 60: print("Pass")       # Skipped.

Output (elif): Only "Excellent" — ONE line printed.

WHY THE DIFFERENCE:
  Multiple `if` = N separate questions asked independently.
  `elif` = a single question with mutually exclusive answers.
  Use `elif` when conditions are on the same variable and only
  ONE outcome should fire.
"""

# ─────────────────────────────────────────────────────────────
# Q2: Triangle Classifier
# ─────────────────────────────────────────────────────────────

def classify_triangle(a, b, c):
    """
    Classifies a triangle given three side lengths.

    Returns:
        str — classification result with reason.
    """
    # Edge case: zero or negative sides
    if a <= 0 or b <= 0 or c <= 0:
        return "Not a triangle — all sides must be positive numbers."

    # Triangle inequality: each side must be < sum of the other two
    if a >= b + c or b >= a + c or c >= a + b:
        return "Not a triangle — violates the triangle inequality theorem."

    # Classification
    if a == b == c:
        return "Equilateral — all three sides are equal."
    elif a == b or b == c or a == c:
        return "Isosceles — exactly two sides are equal."
    else:
        return "Scalene — all three sides are different."


# ── Test Cases ───────────────────────────────────────────────
print("Q2: Triangle Classifier")
print("-" * 45)
test_cases = [
    (5,   5,   5),     # Equilateral
    (5,   5,   8),     # Isosceles
    (3,   4,   5),     # Scalene
    (1,   2,   3),     # Not a triangle (1 + 2 = 3, degenerate)
    (0,   4,   5),     # Zero side
    (-1,  3,   4),     # Negative side
    (10,  1,   1),     # Impossible triangle
]

for a, b, c in test_cases:
    print(f"  classify_triangle({a}, {b}, {c}) → {classify_triangle(a, b, c)}")


# ─────────────────────────────────────────────────────────────
# Q3: Debug / Analyze
# ─────────────────────────────────────────────────────────────
"""
BUGGY CODE:
    score = 85
    if score >= 60: grade = 'D'
    if score >= 70: grade = 'C'
    if score >= 80: grade = 'B'
    if score >= 90: grade = 'A'
    print(grade)

THE BUG:
    All four `if` statements are independent. For score = 85:
      - score >= 60 → True  → grade = 'D'
      - score >= 70 → True  → grade = 'C'  (overwrites 'D')
      - score >= 80 → True  → grade = 'B'  (overwrites 'C')
      - score >= 90 → False → skipped
    Final grade = 'B' (correct here by luck, but wrong approach).

    For score = 100:
      All four conditions are True → grade ends up as 'A' (coincidentally correct).

    The REAL problem: for score = 92, grade would be 'A' ✅ 
    but for score = 65, grade would be 'C' ✗ (should be 'D').
    Wait — let's trace 65: >=60 True→D, >=70 False, >=80 False, >=90 False → 'D' ✅
    
    The actual scenario that BREAKS it: score = 75.
      >=60→D, >=70→C, >=80 False, >=90 False → grade = 'C' ✗ (should be 'C') 
    
    Clearer broken case: Any score ≥ 60 ALWAYS has grade overwritten by each
    subsequent True condition. The logic produces correct output only by accident
    because the conditions are ordered lowest-to-highest and grade keeps getting
    overwritten. The intent is wrong even if the numeric output happens to match.

WHY IT HAPPENS:
    Multiple `if` evaluates ALL conditions independently.
    Each True condition overwrites `grade`. The LAST True condition wins.
    This only works correctly when conditions are ordered from LOW → HIGH.
    If re-ordered (e.g., >=90 first), it would break completely.

CORRECT FIX — use elif with highest threshold first:
"""

print("\nQ3: Bug Fix Demonstration")
print("-" * 45)

score = 85

# Buggy version (shows how it works by accident for some inputs)
if score >= 60: grade = 'D'
if score >= 70: grade = 'C'
if score >= 80: grade = 'B'
if score >= 90: grade = 'A'
print(f"  Buggy code   (score={score}): grade = '{grade}'")

# Fixed version
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f"  Fixed code   (score={score}): grade = '{grade}'")
print()
