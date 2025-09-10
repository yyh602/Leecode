"題目：給定一個整數數組nums 和一個整數target，傳回兩個數字的索引，使得它們加起來等於target。

您可以假設每個輸入只有一個解決方案，並且您可能不會兩次使用相同的元素。

您可以按任意順序返回答案。"



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}   #建立空的雜湊表
        n = len(nums) #獲取陣列的長度，方便後續迴圈使用

        for i in range(n):   #開始遍歷陣列 nums , i 代表當前元素的索引
        
            complement = target - nums[i]     #計算我們需要的「另一半」數字

            if complement in numMap:   #在雜湊表查找
                
                #如果找到，直接回傳兩個數字的索引
                return [numMap[complement],i]  

            numMap[nums[i]] = i      ##如果沒找到，將當前數字及其索引存入雜湊表

        return []   #no solution found
