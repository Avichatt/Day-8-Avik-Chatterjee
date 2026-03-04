# ============================================================
# PART D: AI-Augmented Task — PAN Card Validator
# Day 8 Assignment | codewithnavaid
# ============================================================

# ── EXACT PROMPT USED ────────────────────────────────────────
"""
PROMPT SUBMITTED TO CLAUDE:

"Write a Python program that validates an Indian PAN card number format
using if-else conditions. PAN format: 5 uppercase letters, 4 digits,
1 uppercase letter (e.g., ABCDE1234F). The 4th character indicates
the type of taxpayer."
"""

# ── AI-GENERATED CODE (Claude's output) ─────────────────────
def validate_pan_ai_version(pan):
    """AI-generated version — for critique purposes."""
    pan = pan.upper().strip()

    if len(pan) != 10:
        return False, "Invalid: PAN must be exactly 10 characters"

    # Check first 3 characters are uppercase letters
    for i in range(3):
        if not pan[i].isalpha():
            return False, f"Invalid: Position {i+1} must be a letter"

    # Check 4th character (taxpayer type)
    taxpayer_types = {
        'P': 'Individual',
        'C': 'Company',
        'H': 'Hindu Undivided Family',
        'F': 'Firm',
        'A': 'Association of Persons',
        'T': 'Trust',
        'B': 'Body of Individuals',
        'L': 'Local Authority',
        'J': 'Artificial Juridical Person',
        'G': 'Government',
    }
    if pan[3] not in taxpayer_types:
        return False, f"Invalid: 4th character '{pan[3]}' is not a valid taxpayer type"

    # Check 5th character is uppercase letter
    if not pan[4].isalpha():
        return False, "Invalid: Position 5 must be a letter"

    # Check characters 6-9 are digits
    for i in range(5, 9):
        if not pan[i].isdigit():
            return False, f"Invalid: Position {i+1} must be a digit"

    # Check last character is uppercase letter
    if not pan[9].isalpha():
        return False, "Invalid: Position 10 must be a letter"

    return True, f"Valid PAN — Taxpayer type: {taxpayer_types[pan[3]]}"


# ── CRITICAL EVALUATION ──────────────────────────────────────
"""
EVALUATION OF AI-GENERATED CODE:

1. Are all positions validated correctly?
   ✅ Yes — all 10 positions are checked in the correct order.
   ⚠ Minor: The 4th character check is good, but positions 1–3 and 5
     are checked letter-by-letter; this works but is verbose.

2. Are edge cases handled?
   ⚠ Partially. The code handles:
     ✅ Wrong length
     ✅ Non-alpha in letter positions
     ✅ Non-digit in digit positions
     ✅ Invalid taxpayer type in position 4
   ❌ Does NOT handle:
     - Empty string input → len("") = 0, error message OK, but no crash guard
     - None input → would crash on .upper()
     - Mixed case input is handled (upper() called at start) ✅

3. Is the approach correct (character-by-character vs regex)?
   ⚠ Character-by-character works, but is verbose for a pattern this
     well-defined. A regex like r'^[A-Z]{3}[PCHFATBLJG][A-Z]\d{4}[A-Z]$'
     is far more Pythonic and concise for format validation.
     The taxpayer map is a good addition that regex alone can't do.

4. Is the code Pythonic?
   ⚠ Not fully:
     - Manual for-loops over character positions → should use slicing + str methods
     - Could use str.isalpha() on slices instead of per-character loops
     - The function is fairly readable, but can be more concise.
"""

# ── IMPROVED VERSION ─────────────────────────────────────────
import re

TAXPAYER_TYPES = {
    'P': 'Individual',
    'C': 'Company',
    'H': 'Hindu Undivided Family',
    'F': 'Firm',
    'A': 'Association of Persons (AOP)',
    'T': 'Trust',
    'B': 'Body of Individuals (BOI)',
    'L': 'Local Authority',
    'J': 'Artificial Juridical Person',
    'G': 'Government',
}

PAN_PATTERN = re.compile(r'^[A-Z]{3}[PCHFATBLJG][A-Z]\d{4}[A-Z]$')


def validate_pan(pan):
    """
    Improved PAN validator — combines regex for format + dict for semantic check.

    Improvement over AI version:
      - Handles None and non-string input safely.
      - Uses regex for concise, readable format validation.
      - Separates format check from semantic (taxpayer type) check clearly.
      - Returns a structured result dict for easy consumption.
    """
    # Guard against None / non-string input
    if not isinstance(pan, str):
        return {"valid": False, "reason": "Input must be a string."}

    pan = pan.strip().upper()

    if not pan:
        return {"valid": False, "reason": "PAN cannot be empty."}

    if len(pan) != 10:
        return {"valid": False, "reason": f"PAN must be 10 characters (got {len(pan)})."}

    if not PAN_PATTERN.match(pan):
        # Give a specific reason by checking each segment
        if not pan[:3].isalpha():
            reason = "First 3 characters must be uppercase letters."
        elif pan[3] not in TAXPAYER_TYPES:
            reason = f"4th character '{pan[3]}' is not a valid taxpayer type code."
        elif not pan[4].isalpha():
            reason = "5th character must be an uppercase letter."
        elif not pan[5:9].isdigit():
            reason = "Characters 6–9 must be digits."
        elif not pan[9].isalpha():
            reason = "10th character must be an uppercase letter."
        else:
            reason = "Invalid PAN format."
        return {"valid": False, "reason": reason}

    taxpayer = TAXPAYER_TYPES[pan[3]]
    return {
        "valid": True,
        "pan": pan,
        "taxpayer_type_code": pan[3],
        "taxpayer_type": taxpayer,
        "reason": f"Valid PAN — Taxpayer: {taxpayer}",
    }


# ── Test Cases ────────────────────────────────────────────────
print("PART D: PAN Card Validator — Improved Version")
print("=" * 55)

test_pans = [
    "ABCPE1234F",   # Valid — Individual (P = Individual)
    "AAAPZ1234C",   # Valid — Individual
    "abcpe1234f",   # Valid (lowercase input, auto-uppercased)
    "ABCDE123F",    # Too short
    "ABCDE12345",   # Last char not letter
    "1BCDE1234F",   # First char not letter
    "ABCXE1234F",   # 4th char X — invalid taxpayer type
    "ABCDE123GF",   # Digit in position 9 replaced by letter
    "",             # Empty string
    None,           # None input
    "ABC DE1234F",  # Space inside
]

for pan in test_pans:
    result = validate_pan(pan)
    status = "✅ VALID" if result["valid"] else "❌ INVALID"
    print(f"  {str(pan):<15} → {status} | {result['reason']}")

print()
