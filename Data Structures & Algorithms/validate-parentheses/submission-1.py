class Solution:
    def isValid(self, s: str) -> bool:
        paren_list = []
        if s == "":
            return True
        for c in s:
            if len(paren_list) >= 1 and ((paren_list[-1] == "(" and c == ")") or (paren_list[-1] == "{" and c == "}") or (paren_list[-1] == "[" and c == "]")):
                    paren_list.pop()
            else:
                paren_list.append(c)
        if len(paren_list) == 0:
            return True
        return False