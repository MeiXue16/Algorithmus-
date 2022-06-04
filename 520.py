class Solution(object):
    def detectCapitalUse(self, word):
        #全部大写/小写
        if word.isupper() or word.islower():
            return True
        #从第二个字符开始是否全部是小写
        else:
            return word[1:].islower()
      

        """
        :type word: str
        :rtype: bool
        """
