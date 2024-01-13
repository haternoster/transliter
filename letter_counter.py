from collections import Counter


def letter_count(text):
    result = []
    c = Counter(text)
    for item in c.items():
        result += [{item[0]: item[1]}]
    return result


if __name__ == "__main__":
    text = "aa bb"
    result = letter_count(text)
    print(result)
