def eval_expr(expr: str) -> int:
    """Evaluate a simple arithmetic expression with +, * and parentheses, respecting operator precedence."""
    
    # Remove spaces
    expr = expr.replace(" ", "")
    idx = 0

    def parse_expression():
        nonlocal idx
        result = parse_term()
        while idx < len(expr) and expr[idx] == '+':
            idx += 1
            result += parse_term()
        return result

    def parse_term():
        nonlocal idx
        result = parse_factor()
        while idx < len(expr) and expr[idx] == '*':
            idx += 1
            result *= parse_factor()
        return result

    def parse_factor():
        nonlocal idx
        if expr[idx] == '(':
            idx += 1
            val = parse_expression()
            if idx >= len(expr) or expr[idx] != ')':
                raise ValueError("Missing closing parenthesis")
            idx += 1
            return val
        else:
            start = idx
            while idx < len(expr) and expr[idx].isdigit():
                idx += 1
            if start == idx:
                raise ValueError("Expected number")
            return int(expr[start:idx])

    result = parse_expression()
    if idx != len(expr):
        raise ValueError("Unexpected characters at end of expression")
    return result