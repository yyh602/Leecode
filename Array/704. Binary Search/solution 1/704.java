// 解法1：左閉右閉

class Solution {
    public int search(int[] nums, int target) {
        if(target < nums[0] || target > nums[nums.length -1]){
            return -1;
        }

        int left = 0, right = nums.length-1;

        while(left <= right){
            int mid = left + ((right-left) >> 1); 
            // >>，是右移位運算符，在二進位中，將任何數字右移 1 位，就相當於將該數字除以 2 並向下取整

            if(nums[mid] > target){
                right = mid-1;
            }
            else if(nums[mid] < target){
                left = mid+1;
            }
            else{
                return mid;
            }
        }

        return -1;
    }
}
