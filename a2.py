from typing import List

def match(pattern: List[str], source: List[str]) -> List[str]:
    result = []

    blankList = pattern # I like these names better
    filledList = source

    blankIndex = 0  # index for blankList
    filledIndex = 0  # index for filledList

    while blankIndex < len(blankList):
        if blankList[blankIndex] == "_":
            if filledIndex < len(filledList):
                result.append(filledList[filledIndex])
                filledIndex += 1
            else:
                return None  # Not enough words in filledList
            blankIndex += 1
        elif blankList[blankIndex] == "%":
            temp = []
            while filledIndex < len(filledList) and (blankIndex + 1 >= len(blankList) or filledList[filledIndex] != blankList[blankIndex + 1]):
                temp.append(filledList[filledIndex])
                filledIndex += 1
            result.append(" ".join(temp))  # join collected words into a single string
            blankIndex += 1
        else:
            # blankList does not match the filledList
            if filledIndex >= len(filledList) or blankList[blankIndex] != filledList[filledIndex]:
                return None
            blankIndex += 1
            filledIndex += 1

    # check if there's still unmatched words in filledList
    if filledIndex < len(filledList):
        if blankList[-1] == "%":
            result.append("")
        else:
            return None  # too many words in filledList

    return result


if __name__ == "__main__":
    assert match(["x", "y", "z"], ["x", "y", "z"]) == [], "test 1 failed"
    assert match(["x", "z", "z"], ["x", "y", "z"]) == None, "test 2 failed"
    assert match(["x", "y"], ["x", "y", "z"]) == None, "test 3 failed"
    assert match(["x", "y", "z", "z"], ["x", "y", "z"]) == None, "test 4 failed"
    assert match(["x", "_", "z"], ["x", "y", "z"]) == ["y"], "test 5 failed"
    assert match(["x", "_", "_"], ["x", "y", "z"]) == ["y", "z"], "test 6 failed"
    assert match(["%"], ["x", "y", "z"]) == ["x y z"], "test 7 failed"
    assert match(["x", "%", "z"], ["x", "y", "z"]) == ["y"], "test 8 failed"
    assert match(["%", "z"], ["x", "y", "z"]) == ["x y"], "test 9 failed"
    assert match(["x", "%", "y"], ["x", "y", "z"]) == None, "test 10 failed"
    assert match(["x", "%", "y", "z"], ["x", "y", "z"]) == [""], "test 11 failed"
    assert match(["x", "y", "z", "%"], ["x", "y", "z"]) == [""], "test 12 failed"
    assert match(["_", "%"], ["x", "y", "z"]) == ["x", "y z"], "test 13 failed"
    assert match(["_", "_", "_", "%"], ["x", "y", "z"]) == [
        "x",
        "y",
        "z",
        "",
    ], "test 14 failed"
    assert match(["x", "%", "z"], ["x", "y", "z", "z", "z"]) == None, "test 15 failed"

    print("All tests passed!")
