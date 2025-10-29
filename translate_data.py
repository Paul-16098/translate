import json
import re
from Branch import Branch

translate_kv = dict[str, str]
compile_flags = re.I | re.X | re.M


# 定義正則表達式模式及其替換
RegexPatterns: translate_kv = {
    # ...
}
# load from json
with open("./RegexPatterns.json", "rt", encoding="utf-8") as f:
    RegexPatterns.update(json.load(f))

# 預編譯正則表達式模式以提高效率
compiledRegexPatterns = {
    re.compile(k, compile_flags): v for k, v in RegexPatterns.items()
}

RegexPatternsWithBranch: dict[str, set[str]] = (
    Branch({"{1}": {"a", "b", "c"}})
    .add(
        "1",
        {
            r"(\#+) {1}": r"\1 {1} \1",
        },
    )
    .add(
        "2",
        {
            r"\*{1}\*": r"{1}",
        },
    )
    .done_with_zip()
)
# load from json
with open("./RegexPatternsWithBranchVer.json", "rt", encoding="utf-8") as f:
    b = Branch(json.load(f))

with open("./RegexPatternsWithBranch.json", "rt", encoding="utf-8") as f:
    for a in json.load(f):
        b.add(**a)
RegexPatternsWithBranch.update(b.done_with_zip())

compiledRegexPatternsWithBranch: dict[str, set[re.Pattern]] = {}
for v, k in RegexPatternsWithBranch.items():
    for kk in k:
        compiledRegexPatternsWithBranch.setdefault(v, set()).add(
            re.compile(kk, compile_flags)
        )

# 定義直接替換
stringReplacementMap: translate_kv = {
    # ...
}
# load from json
with open("./stringReplacementMap.json", "rt", encoding="utf-8") as f:
    stringReplacementMap.update(json.load(f))

stringReplacementMapWithBranch = (
    Branch()
    .add(
        "...",
        {
            # ...
        },
    )
    .add(
        "...",
        {
            # ...
        },
    )
    .done_with_zip()
)
# load from json
with open("./stringReplacementMapWithBranchVer.json", "rt", encoding="utf-8") as f:
    b = Branch(json.load(f))

with open("./stringReplacementMapWithBranch.json", "rt", encoding="utf-8") as f:
    for a in json.load(f):
        b.add(**a)
RegexPatternsWithBranch.update(b.done_with_zip())
