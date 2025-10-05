# 雙指針法（快慢指針法）：透過一個快指針和慢指針在一個循環完成下兩個循環的工作。

'''
定義快慢指針

快指標：尋找新的儲存元素，新的儲存就是不含目標元素的存儲
慢指標：指向更新新記憶體下的位置
'''

# Time Complexity：O(n)

# Space Complexity：O(1)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0 
        slow = 0
        size = len(nums)
        while fast < size:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
