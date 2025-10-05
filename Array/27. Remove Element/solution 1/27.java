// 暴力破解法

// Time Complexity： O(n^2)

// Space Complexity：O(1)

class Solution {
    public int removeElement(int[] nums, int val) {
        int size = nums.length;

        for(int i=0; i<size; i++){
            if(nums[i] == val){
                for(int j=i+1; j<size; j++){
                    nums[j-1]=nums[j];
                }
                i--;
                size--;
            }
        }
        return size;
    }
}
