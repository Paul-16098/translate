class Branch:
    branch_date: dict[str, dict[str, str]]
    _ver: dict[str, str | list[str] | set[str] | tuple[str]]

    def __init__(
        self, ver: dict[str, str | list[str] | set[str] | tuple[str]] | None = None
    ) -> None:
        # 每個實例獨立的 branch_date
        self.branch_date = {}

        # 初始化版本映射，避免未定義屬性
        self._ver = ver or {}

    def add(self, name: str, date: dict[str, str]):
        self.branch_date[name] = date
        return self

    def remove(self, branch_name: str):
        self.branch_date.pop(branch_name)
        return self

    def ver(self, name: str, value: str | list[str] | set[str] | tuple[str]):
        self._ver[name] = value
        return self

    def done(self) -> dict[str, str]:
        from itertools import product

        result: dict[str, str] = {}
        for date in self.branch_date.values():
            for k, v in date.items():
                if len(self._ver) > 0:
                    keys = [k]
                    values = [v]
                    for vk, vv in self._ver.items():
                        if isinstance(vv, (list, tuple, set)):
                            # 將所有可能的替換組合生成
                            keys = [
                                key.replace(vk, sub) for key, sub in product(keys, vv)
                            ]
                            values = [
                                val.replace(vk, sub) for val, sub in product(values, vv)
                            ]
                        else:
                            keys = [key.replace(vk, vv) for key in keys]
                            values = [val.replace(vk, vv) for val in values]

                    # 將所有組合加入結果
                    for n_k, n_v in zip(keys, values):
                        result[n_k] = n_v
                else:
                    result.update(date)

        return result

    def done_with_zip(self) -> dict[str, set[str]]:
        reverse_map: dict[str, set[str]] = {}
        for k, v in self.done().items():
            reverse_map.setdefault(v, set()).add(k)
        return reverse_map


# 測試用例
assert Branch({"{&1}": {"1", "2"}, "{&2}": {"a", "b"}}).add(
    "n1", {"{&1}|{&2}": "0"}
).done_with_zip() == {"0": {"1|a", "2|a", "1|b", "2|b"}}
assert Branch({"{&1}": {"1", "2"}, "{&2}": {"a", "b"}}).add(
    "n1", {"{&1}|{&2}": "0"}
).done() == {"1|a": "0", "2|a": "0", "1|b": "0", "2|b": "0"}
