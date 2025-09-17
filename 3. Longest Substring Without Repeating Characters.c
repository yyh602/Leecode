#include <stdio.h>    // 包含標準輸入輸出函式庫，用於 printf
#include <string.h>   // 包含字串函式庫，用於 strlen 函式
#include <stdbool.h>  // 包含布林類型函式庫，用於使用 bool 類型

// 自定義一個 max 函式，用於比較兩個整數並返回較大的那個。
int max(int a, int b) {
    return a > b ? a : b;
}

int lengthOfLongestSubstring(char* s) {
    // 使用 strlen 函式取得字串 s 的長度
    int n = strlen(s);

    // 處理特殊情況：如果字串是空的，直接返回 0
    if (n == 0) {
        return 0;
    }

    // 宣告一個布林陣列 charExists，大小為 128。
    // 這 128 個位置代表 ASCII 字元集中的字元（ASCII 碼 0-127）。
    // 陣列元素預設為 false，用於快速檢查某個字元是否已存在於當前的「滑動視窗」中。
    bool charExists[128] = {false};
    
    // 初始化變數
    int maxLength = 0; // 記錄到目前為止找到的最長子字串長度
    int left = 0;      // 滑動視窗的左邊界指標

    // 迴圈遍歷整個字串，right 指標代表滑動視窗的右邊界
    for (int right = 0; right < n; right++) {
        // 當前字元 s[right] 在 charExists 陣列中為 true 時，表示它已經在視窗內出現過
        while (charExists[s[right]]) {
            // 出現重複，需要「縮小」視窗。
            // 將左邊界 s[left] 對應的字元狀態設為 false，表示它被移出視窗
            charExists[s[left]] = false;
            // 將左邊界指標 left 向右移動一位
            left++;
        }
        
        // 當 while 迴圈結束時，代表滑動視窗內已無重複字元
        // 將當前字元 s[right] 加入視窗，將其狀態設為 true
        charExists[s[right]] = true;
        
        // 計算當前滑動視窗的長度 (right - left + 1)，並更新 maxLength
        // 確保 maxLength 始終為所有有效視窗中的最大長度
        maxLength = max(maxLength, right - left + 1);
    }
    
    // 返回最終找到的最長子字串長度
    return maxLength;
}
