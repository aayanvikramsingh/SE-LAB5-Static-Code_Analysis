# Lab 5: Static Code Analysis

## Author

* **Name:** AAYAN VIKRAM SINGH

* **SRN:** PES2UG23CS014

## Objective

The objective of this lab was to take a provided Python program (`inventory_system.py`), analyze it for quality, security, and style issues, and then refactor the code to fix all identified problems.

## Tools Used

* **Pylint:** For in-depth code quality, error detection, and style convention (PEP 8) checking.

* **Bandit:** For identifying common security vulnerabilities.

* **Flake8:** For enforcing PEP 8 style, checking for syntax errors, and finding logical inconsistencies.

* **GitHub Codespaces:** As the all-in-one development environment.

## Summary of Work

1. **Initial Analysis:** The original `inventory_system.py` was analyzed using all three tools. This generated initial reports showing numerous critical security flaws, bugs, and style violations, resulting in an initial Pylint score of **4.80/10**.

2. **Iterative Refactoring:** The code was fixed in multiple passes. Each fix was verified by re-running the tools, which often revealed more subtle issues that were previously hidden.

3. **Final Verification:** The process was repeated until all tools reported zero issues.

## Key Issues Identified and Fixed

The refactoring process addressed every issue flagged by the tools, including:

* **Security (Bandit: B307):** Removed a dangerous `eval()` function call.

* **Critical Bug (Pylint: W0102):** Fixed a "Dangerous Default Value" bug by replacing a mutable list (`[]`) in function arguments with `None`.

* **Robustness (Flake8: E722):** Replaced a high-risk bare `except:` block with a specific `except KeyError:`.

* **Design (Pylint: W0603):** Correctly refactored the `load_data` function to modify the global state in-place (using `.clear()` and `.update()`) instead of using the problematic `global` keyword.

* **Readability (Pylint/Flake8):** Added docstrings to the module and all functions, fixed all naming conventions (e.g., `addItem` to `add_item`), and corrected all whitespace, line length, and formatting errors.

## Final Result

The fully refactored `inventory_system.py` now passes all static analysis checks with a perfect score.

* **Pylint Score:** **10.00/10**

* **Bandit Report:** No issues identified.

* **Flake8 Report:** No issues identified.

The final code is secure, robust, and compliant with all PEP 8 style conventions.