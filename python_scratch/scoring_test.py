
def complex_rule(value):
    if not value:
        return 0
    if value == "many":
        return 6
    if type(value) is int:
        return value // 10
    return 1


rules = [
    10,
    20,
    5,
    lambda value: value * 15,
    lambda value: (value in ["x", "y"]) * 1000,
    complex_rule
]


thresholds = [(0, "low"), (10, "high"), (20, "immediate")]


def score(answers):
    if not answers:
        answers = []
    return sum(r * a if type(r) is int else r(a) for r, a in zip(rules, answers))


def assign_risk(calculated_score: int):
    out_str = "no"
    for k, v in thresholds:
        if calculated_score >= k:
            out_str = v
        else:
            break
    return f"{out_str} risk"


def process(answers=None):
    return assign_risk(score(answers))


if __name__ == "__main__":
    print(process([True, False, False, False, "a"]))
    print(process([False, False, False, False, "x"]))
    print(process([False, False, False, True, "a"]))
    print(process([False, False, False, False, "a"]))
    print(process([False, False, False, False, "a", 500]))
    print(process([False, False, False, False, "a", "many"]))
    print(process([False, False, False, True, "a", "many"]))
    print(process([]))
    print(process())
