// 解法1：定義target是在一個左閉右閉的區間裡，也就是[left,right]

// Time Complexity：O(log n)
// 二分搜尋的核心是：每執行一次迴圈，都會將目前的搜尋範圍減少大約一半。

// Space Complexity：O(1)
/* 因為所需的額外空間是固定且有限的常數，程式碼中只使用了幾個額外的變數來儲存狀態：
    left (整數)
    right (整數)
    middle (整數)
  這些變數的數量是固定的，與輸入陣列 n 的大小無關
*/

class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left=0;
        int right=nums.size()-1;

        while(left <= right){
            int middle=(left+right)/2;
            if(nums[middle] > target){
                right=middle-1;
            }
            else if(nums[middle] < target){
                left=middle+1;
            }
            else{
                return middle;
            }
        }

        return -1;
    }
};
