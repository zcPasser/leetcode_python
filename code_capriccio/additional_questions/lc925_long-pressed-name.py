class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        len_name, len_typed = len(name), len(typed)
        if len_name > len_typed:
            return False
        idx_name, idx_typed = 0, 0
        while idx_name < len_name and idx_typed < len_typed:
            if name[idx_name] == typed[idx_typed]:
                if idx_typed + 1 < len_typed and typed[idx_typed] == typed[idx_typed + 1]:
                    while idx_typed + 1 < len_typed and typed[idx_typed] == typed[idx_typed + 1]:
                        idx_typed += 1
                        if idx_name + 1 < len_name and name[idx_name] == name[idx_name + 1]:
                            idx_name += 1
                else:
                    idx_name += 1
                    idx_typed += 1
            else:
                return False

        return idx_name == len_name and idx_typed == len_typed