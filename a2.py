from typing import List
import re

def match(pattern: List[str], source: List[str]) -> List[str]:
    """Attempts to match the pattern to the source.

    % matches a sequence of zero or more words and _ matches any single word

    Args:
        pattern - a pattern using to % and/or _ to extract words from the source
        source - a phrase represented as a list of words (strings)

    Returns:
        None if the pattern and source do not "match" ELSE A list of matched words
        (words in the source corresponding to _'s or %'s, in the pattern, if any)
    """
    result = []
    
    if pattern == ["%"]:
        return [" ".join(source)]

    i = 0  # index for pattern
    j = 0  # index for source

    while i < len(pattern) and j < len(source):
        if pattern[i] == "_":
            result.append(source[j])
            i += 1
            j += 1
        elif pattern[i] == "%":
            # Consume all words until we hit a pattern part or end of source
            while j < len(source) and (i + 1 < len(pattern) and pattern[i + 1] != source[j]):
                result.append(source[j])
                j += 1
            # Move past the % in the pattern
            i += 1
        else:
            if pattern[i] != source[j]:
                return None  # mismatch
            i += 1
            j += 1

    # Check for remaining pattern parts
    while i < len(pattern) and pattern[i] == "%":
        result.append("")  # Add empty for trailing % in pattern
        i += 1

    # If there's still unmatched pattern parts, return None
    if i < len(pattern) or j < len(source):
        return None


    return result

# Testing assertions
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
