#方法1 - Set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0       #追蹤目前遇到的最長子字串的長度
        charSet = set()     #用來追蹤當前字串中的唯一字元
        left = 0
        
        for right in range(n):
            if s[right] not in charSet:    #如果目前字元不在集合（charSet）中，則表示我們有一個新的唯一字元
                charSet.add(s[right])      #將字元插入集合中
                maxLength = max(maxLength, right - left + 1)  #並更新maxLength
            else:
                while s[right] in charSet:  #如果該字元已經存在於集合中，則表示目前子字串中的重複字元
                    charSet.remove(s[left]) #將left指針向前移動，從集合中刪除字符，直到重複字符不再存在
                    left += 1
                charSet.add(s[right])   #將當前字元插入集合並繼續迭代
        
        return maxLength
