// 暴力破解法：兩層 for 迴圈，第一個for走訪陣列元素，第二個for更新陣列

// Time Complexity： O(n^2)

// Space Complexity：O(1)

class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int size = nums.size(); // 初始化為輸入向量 nums 的當前長度。
                                // 這個變數將在程式執行過程中記錄有效元素（即不等於 val 的元素）的數量，並在每次移除一個元素時遞減

        for(int i=0; i<size; i++){
            if(nums[i]==val){ // 發現需要移除的元素, 所以將陣列集體向前移動一位

                // 內層迴圈，它負責「移除」的操作
                // 由於不能真的從底層陣列中刪除元素，它的做法是將所有在索引 i 之後的元素向前移動一位，從而覆蓋掉位於 nums[i] 的目標值
                for(int j=i+1; j<size; j++){
                    nums[j-1] = nums[j];
                }

                // 因為整個陣列都被向前移動了一位，原本位於 i+1 的元素現在跑到了 i 的位置
                i--;

                // 成功「移除」了一個元素，所以有效元素的總數減一
                size--;
            }
        }
        return size;
    }
};
