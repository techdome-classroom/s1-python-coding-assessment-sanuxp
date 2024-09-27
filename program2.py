def decode_message( s: str, p: str) -> bool:
        len1, len2, mat, star = 0, 0, 0, -1
        while len1<len(s):
                if len2<len(p) and (p[len2]=='?' or p[len2] == s[len1]):
                        len1+=1
                        len2+=1
                elif len2<len(p) and p[len2]=='*':
                        star = len2
                        mat = len1
                        len2+=1
                elif star!=-1:
                        len2 = star+1
                        mat+=1
                        len1 = mat
                else: return False
        while len2<len(p) and p[len2] == '*':
                len2+=1
        return len2 == len1