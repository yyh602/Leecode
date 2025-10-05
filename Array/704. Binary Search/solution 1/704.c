// 解法1：左閉佑閉

// Time Complexity：O(log n)

// Space Complexity：O(1)

int search(int* nums, int numsSize, int target) {
    int left = 0;
    int right = numsSize-1;
    int mid = 0;

    while (left<=right){
        mid = (left+right)/2;

        if(nums[mid]>target){
            right = mid-1;
        }
        else if(nums[mid]<target){
            left = mid+1;
        }
        else{
            return mid;
        }
    }
    return -1;
}
