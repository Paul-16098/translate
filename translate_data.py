import re
from Branch import Branch

translate_kv = dict[str, str]
compile_flags = re.I | re.X | re.M


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
compiledRegexPatternsWithBranch: dict[str, set[re.Pattern]] = {}
for k, v in RegexPatternsWithBranch.items():
    for kk in v:
        compiledRegexPatternsWithBranch.setdefault(k, set()).add(
            re.compile(kk, compile_flags)
        )


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
