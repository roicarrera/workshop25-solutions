def main(word):
    high_letters = set("tdfhklb")
    low_letters = set("qypgj")
    highs = sum(1 for c in word if c in high_letters)
    lows = sum(1 for c in word if c in low_letters)
    if highs > lows:
        return "high"
    elif lows > highs:
        return "low"
    else:
        return "medium"