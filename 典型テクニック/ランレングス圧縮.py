from itertools import groupby


# Helper function for run length encoding
def _groupby_helper(S: str):
    return [(k, len(list(v))) for k, v in groupby(S)]


# RUN LENGTH ENCODING str -> list[tuple(str, int)]
# example) "aabbbbaaca" -> [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)]
def runLengthEncode(S: str) -> list[tuple[str, int]]:
    return _groupby_helper(S)


# RUN LENGTH DECODING list[tuple] -> str
# example) [('a', 2), ('b', 4), ('a', 2), ('c', 1), ('a', 1)] -> "aabbbbaaca"
def runLengthDecode(L: list[tuple]) -> str:
    return "".join(c * n for c, n in L)


# RUN LENGTH ENCODING str -> str
# example) "aabbbbaaca" -> "a2b4a2c1a1"
def runLengthEncodeToString(S: str) -> str:
    return "".join(f"{k}{n}" for k, n in _groupby_helper(S))


print(runLengthEncode("aaAAAiiiiIIIuuUuu"))
print(runLengthEncodeToString("aaAAAiiiiIIIuuUuu"))
