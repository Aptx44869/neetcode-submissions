class Solution:
    def isValid(self, s: str) -> bool:
        st=[]
        pairs={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for ch in s:
            if ch in pairs:
                if st and st[-1]== pairs[ch]:
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)
        return not st