class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)  #取得輸入字串 s 的長度

        #初始化一個 n x n 的二維布林陣列 dp
        #dp[i][j] 將用於記錄從索引 i 到 j 的子字串是否為回文
        dp = [[False] * n for _ in range(n)]

        #初始化 ans 陣列，它將儲存目前找到的最長回文子字串的起始和結束索引
        #預設為 [0, 0]，代表單個字元（因為任何單一字元都是回文)
        ans = [0, 0]

        #遍歷字串中的每個字元，將所有長度為 1 的子字串標記為回文
        for i in range(n):
            dp[i][i] = True  #單一字元本身就是一個回文，所以 dp[i][i] 設為 True

        #遍歷所有長度為 2 的子字串
        for i in range(n - 1):

            #如果相鄰的兩個字元相等，則它們構成一個回文
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True  #將 dp[i][i + 1] 設為 True
                ans = [i, i + 1]    #同時更新 ans，因為這是目前找到的最長回文（長度為 2）

        #diff 代表子字串的長度減 1，這個迴圈從長度 3 開始，逐步檢查更長的子字串
        for diff in range(2, n):

            #遍歷所有可能的起始索引 i
            for i in range(n - diff):
                j = i + diff  #計算對應的結束索引 j

                #檢查 s[i] 和 s[j] 是否相等，
                #同時檢查它們內部的子字串（從 i+1 到 j-1）是否為回文
                #這就是動態規劃的遞迴關係：
                #一個子字串是回文，若且唯若它的兩端字元相等，且其內部子字串也是回文
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True  #如果條件成立，將 dp[i][j] 標記為 True
                    ans = [i, j]     #同時更新 ans，因為我們找到了一個更長的回文子字串

        i, j = ans  #從 ans 中取出最長回文子字串的起始和結束索引

        return s[i : j + 1] #根據索引 i 和 j，從原始字串 s 中切割出最長的回文子字串並返回
