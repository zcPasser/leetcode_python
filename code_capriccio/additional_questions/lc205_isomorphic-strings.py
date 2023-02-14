class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sch_to_tch = dict()
        tch_to_sch = dict()
        len_s = len(s)
        for i in range(len_s):
            if s[i] not in sch_to_tch:
                sch_to_tch[s[i]] = t[i]
            if t[i] not in tch_to_sch:
                tch_to_sch[t[i]] = s[i]
            if sch_to_tch[s[i]] != t[i] or tch_to_sch[t[i]] != s[i]:
                return False
        return True