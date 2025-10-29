from translate_data import (
    compiledRegexPatterns,
    stringReplacementMap,
    compiledRegexPatternsWithBranch,
    stringReplacementMapWithBranch,
)

import re


# 初始化 Pattern_match_status：使用可辨識的字串 value
Pattern_match_status: dict[str, int] = {}

for cp in compiledRegexPatterns.values():
    Pattern_match_status[cp] = 0
for s_key in stringReplacementMap.values():
    Pattern_match_status[s_key] = 0

for k in compiledRegexPatternsWithBranch.keys():
    Pattern_match_status[k] = 0
for k in stringReplacementMapWithBranch.keys():
    Pattern_match_status[k] = 0


# 讀取輸入文件
def read_file(file_path):
    """Read the content of a file."""
    with open(file_path, "rt", encoding="utf-8") as f:
        return f.read()


# 寫入輸出文件
def write_file(file_path: str, content: str):
    """Write content to a file."""
    with open(file_path, "wt", encoding="utf-8") as f:
        f.write(content)


# 應用正則表達式替換
def apply_regex_replacements(content: str, patterns: dict[re.Pattern[str], str]):
    """Apply regex-based replacements to the content."""
    for compiled_pattern, replacement in patterns.items():
        matches = compiled_pattern.findall(content)  # 找到所有匹配
        match_count = len(matches)  # 計算匹配次數
        if match_count == 0:
            continue
        content = compiled_pattern.sub(replacement, content)  # 替換內容
        Pattern_match_status[replacement] += match_count  # 累加匹配次數
    return content


def apply_regex_replacements_with_branch(
    content: str, patterns: dict[str, set[re.Pattern[str]]]
):
    """Apply regex-based replacements to the content."""
    for v, k_s in patterns.items():
        for k in k_s:
            matches = k.findall(content)  # 找到所有匹配
            match_count = len(matches)  # 計算匹配次數
            if match_count == 0:
                continue
            Pattern_match_status[v] += match_count  # 累加匹配次數
            content = k.sub(v, content)  # 替換內容
    return content


# 應用直接替換
def apply_direct_replacements(content: str, replacements: dict[str, str]):
    """Apply direct string replacements to the content."""
    for old, new in replacements.items():
        match_count = content.count(old)  # 計算字符串出現次數
        if match_count == 0:
            continue
        Pattern_match_status[new] += match_count  # 累加匹配次數
        content = content.replace(old, new)  # 替換內容
    return content


def apply_direct_replacements_with_branch(
    content: str, replacements: dict[str, set[str]]
):
    """Apply direct string replacements to the content."""
    for new, olds in replacements.items():
        for old in olds:
            match_count = content.count(old)  # 計算字符串出現次數
            if match_count == 0:
                continue
            Pattern_match_status[new] += match_count  # 累加匹配次數
            content = content.replace(old, new)  # 替換內容
    return content


# 主處理函數
def process_files(input_path: str, output_path: str):
    """Process the input file, apply replacements, and save results."""
    content = read_file(input_path)  # 讀取輸入文件

    content = apply_regex_replacements_with_branch(
        content, compiledRegexPatternsWithBranch
    )

    # 應用正則表達式替換
    content = apply_regex_replacements(content, compiledRegexPatterns)

    # 保存中間結果
    # write_file("sep1.txt", content)

    content = apply_direct_replacements_with_branch(
        content, stringReplacementMapWithBranch
    )

    # 應用直接替換
    content = apply_direct_replacements(content, stringReplacementMap)

    write_file(
        output_path,
        content,
    )  # 保存最終結果


# 文件路徑
input_file = "./raw.txt"  # 輸入文件路徑
output_file = "./out.txt"  # 輸出文件路徑


# 執行處理
process_files(input_file, output_file)  # 運行處理管道


# 匹配狀態輸出
def print_match_status():
    """Print the match status for all patterns and replacements."""
    print("\nPattern Match Status:")
    # print(Pattern_match_status)
    for key, count in sorted(
        Pattern_match_status.items(), key=lambda t: t[1], reverse=True
    ):
        print(f"{key!r}: {count} matches")


# 打印匹配狀態
print_match_status()
