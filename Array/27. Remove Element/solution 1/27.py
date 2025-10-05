# 暴力破解法

# Time Complexity： O(n^2)

# Space Complexity：O(1)

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i, size = 0, len(nums)
        while i < size:
            if nums[i] == val: # 找到等於目標值的節點
                for j in range(i+1, size): # 移除該元素，並將後方元素向前平移
                    nums[j - 1] = nums[j]
                size -= 1
                i -= 1
            i += 1
        return size   
