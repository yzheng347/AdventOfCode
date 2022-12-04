from collections import Counter

def count_rep(digits):
    counter = Counter(digits)
    return counter.values()

def no_desc(digits):
    return sorted(digits) == digits


if __name__ == "__main__":
    result = 0
    for i in range(138241,674034):
        digits = [int(x) for x in str(i)]
        if no_desc(digits) and 2 in count_rep(digits):
        # if no_desc(digits) and max(count_rep(digits)) >= 2:
            result += 1
    print(f"Res: {result}")
