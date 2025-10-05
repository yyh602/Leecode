// 雙指針法（快慢指針法）：透過一個快指針和慢指針在一個循環完成下兩個循環的工作。

/* 定義快慢指針

    快指標：尋找新的儲存元素，新的儲存就是不含目標元素的存儲
    慢標指標：指向更新新記憶體下的位置
*/

// Time Complexity：O(n)

// Space Complexity：O(1)

class Solution {
    public int removeElement(int[] nums, int val) {
        int slow = 0;
        int size = nums.length;
        for(int fast=0; fast<size; fast++){
            if(val != nums[fast]){
                nums[slow++] = nums[fast];
            }
        }
        return slow;  
    }
}
