def eval_expr(expr: str) -> int:
    """Evaluate a simple arithmetic expression containing +, * and parentheses."""
    # Remove whitespace
    expr = expr.replace(" ", "")
    # Handle parentheses by recursion: find innermost, evaluate it, substitute back
    open_idx = expr.rfind("(")
    if open_idx != -1:
        close_idx = expr.find(")", open_idx)
        # Recursively evaluate the inside of the parentheses
        inner_value = eval_expr(expr[open_idx+1:close_idx])
        # Replace the "(...)" with its value and evaluate the resulting string
        new_expr = expr[:open_idx] + str(inner_value) + expr[close_idx+1:]
        return eval_expr(new_expr)
    # No parentheses left at this point. Parse and evaluate left-to-right.
    tokens = []
    number = ""
    for ch in expr:
        if ch.isdigit():
            number += ch  # build multi-digit numbers
        else:
            # ch is an operator (assume only + or *)
            if number == "":
                raise ValueError("Invalid expression syntax")
            tokens.append(int(number))
            tokens.append(ch)
            number = ""
    if number:
        tokens.append(int(number))
    # Now evaluate the tokens sequentially
    if not tokens:
        return 0
    result = tokens[0]
    i = 1

    # First loop only multiplications
    while i < len(tokens):
        op = tokens[i]; val = tokens[i+1]
        if op == "+":
            i +=1
        elif op == "*":
            result = result * val
            i += 2
    # Second loop only remaining addition
    i = 1
    while i < len(tokens):
        op = tokens[i]; val = tokens[i+1]
        if op == "+":
            result = result + val
            i += 2
        elif op == "*":
            i +=1

    return result