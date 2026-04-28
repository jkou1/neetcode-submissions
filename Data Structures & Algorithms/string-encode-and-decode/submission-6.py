class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += "`" + s + "`"
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        tf = False
        curString = ""
        for char in s:
            if tf:
                if char == '`':
                    tf = False
                    res.append(curString)
                    curString = ""
                    continue
                else:
                    curString += char

            elif char == '`':
                tf = True
                continue
        return res

