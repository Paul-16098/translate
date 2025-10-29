import json


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

    @staticmethod
    def import_from_file(brach_path="Branch.json", ver_path="BranchVer"):
        with open(ver_path, "rt", encoding="utf-8") as f:
            ver = json.load(f)
        with open(brach_path, "rt", encoding="utf-8") as f:
            bd = json.load(f)
        return Branch.import_from_json(bd, ver)

    @staticmethod
    def import_from_json(
        branch_json: dict[str, dict[str, str]],
        ver_json: dict[str, str | list[str] | set[str] | tuple[str]],
    ):
        b = Branch(ver_json)
        b.branch_date = branch_json
        return b

    def export_to_file(
        self,
        brach_path="Branch.json",
        ver_path="BranchVer",
    ):
        ver = {}
        for k, v in self._ver.items():
            if isinstance(v, (str)) or isinstance(v, (tuple, list)):
                ver[k] = v
            elif isinstance(v, (set)):
                ver[k] = tuple(v)
        with open(ver_path, "wt", encoding="utf-8") as f:
            json.dump(ver, f, ensure_ascii=False)
        with open(brach_path, "wt", encoding="utf-8") as f:
            json.dump(self.branch_date, f, ensure_ascii=False)
        return self


# 測試用例
assert Branch({"{&1}": {"1", "2"}, "{&2}": {"a", "b"}}).add(
    "n1", {"{&1}|{&2}": "0"}
).done_with_zip() == {"0": {"1|a", "2|a", "1|b", "2|b"}}
assert Branch({"{&1}": {"1", "2"}, "{&2}": {"a", "b"}}).add(
    "n1", {"{&1}|{&2}": "0"}
).done() == {"1|a": "0", "2|a": "0", "1|b": "0", "2|b": "0"}
