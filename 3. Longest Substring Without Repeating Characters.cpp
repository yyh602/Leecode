class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        int maxLength = 0;     //追蹤目前遇到的最長子字串的長度
        unordered_set<char> charSet;   //用來追蹤當前字串中的唯一字元
        int left = 0;

        for(int right = 0; right <n; right++){
            if (charSet.count(s[right]) == 0) {    //如果目前字元不在集合（charSet）中，則表示我們有一個新的唯一字元
                charSet.insert(s[right]);           //將字元插入集合中
                maxLength = max(maxLength, right - left + 1);  //並更新maxLength
            } else {
                while (charSet.count(s[right])) {   //如果該字元已經存在於集合中，則表示目前子字串中的重複字元
                    charSet.erase(s[left]);      //將left指針向前移動，從集合中刪除字符，直到重複字符不再存在
                    left++;
                }
                charSet.insert(s[right]);   //將當前字元插入集合並繼續迭代
            }
        }

        
        return maxLength;
    }
};
