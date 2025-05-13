def reverse(xs: list) -> list:
    return [xs[i] for i in range(len(xs)-1, -1, -1)]

def sort(xs: list) -> list:
    return sorted(xs)

def deduplicate(xs: list) -> list:
    seen = set()
    result = []
    for x in xs:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result