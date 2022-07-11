class Solution:
    def isUnique(self, astr: str) -> bool:
        mark = 0
        for i in astr:
            movebit = ord(i) -ord('a')
            if mark & (1<< movebit): # 位运算0000 & 0010 =0， 0010 & 0011 =1, movebit=1
                return False
            else:
                mark = mark | (1<< movebit) # 0000 | 0010 =0010
        return True
