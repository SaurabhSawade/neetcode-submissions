class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        # if s[0] == "]" or s[0] == "}" or s[0] == ")" :
        #     return False
        for char in s:
            if char == "[" or char == "{" or char == "(":
                st.append(char)
            elif char == ")":
                if len(st) == 0 or st[-1] != "(":
                    return False
                st.pop()
            elif char == "}":
                if len(st) == 0 or st[-1] != "{":
                    return False
                st.pop()
            elif char == "]":
                if len(st) == 0 or st[-1] != "[":
                    return False
                st.pop()
        if st :
            return False
        return True