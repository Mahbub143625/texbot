import re

def solve_textile_math(expression):
    """Solves textile-related math problems step by step."""
    try:
        # Clean the expression and detect textile-related keywords
        if "gsm" in expression.lower():
            return solve_gsm_problem(expression)
        expression_cleaned = re.sub(r'[=?ans?\s]+$', '', expression)
        result = eval(expression_cleaned)
        return f"Step-by-step solution: {expression_cleaned} = {result}"
    except Exception as e:
        return "There was an error solving the math problem."

def solve_gsm_problem(expression):
    """Solves GSM-related textile math problems."""
    try:
        # Example: "Calculate GSM for a 3000-meter fabric weighing 500 grams"
        result = "GSM calculation steps"
        return result
    except Exception:
        return "There was an error with the GSM problem."
