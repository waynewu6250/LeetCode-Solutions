#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        if len(path) == 0:
            return ""
        
        st = []
        for item in path.split("/"):
            if item == "" or item == ".":
                continue
            if item == "..":
                if st:
                    st.pop(-1)
            else:
                st.append(item)


        return "/" + "/".join(st)
        

