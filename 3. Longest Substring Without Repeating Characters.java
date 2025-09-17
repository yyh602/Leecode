class Solution {
    public int lengthOfLongestSubstring(String s) {
        int n = s.length();  
        int maxLength = 0;    //追蹤目前遇到的最長子字串的長度
        Set<Character> charSet = new HashSet<>();  //用來追蹤當前字串中的唯一字元
        int left = 0;

        for (int right=0; right<n; right++){
            if (!charSet.contains(s.charAt(right))) {   //如果目前字元不在集合（charSet）中，則表示我們有一個新的唯一字元
                charSet.add(s.charAt(right));    //將字元插入集合中
                maxLength = Math.max(maxLength, right - left + 1);  //並更新maxLength
            } else {
                while (charSet.contains(s.charAt(right))) {  //如果該字元已經存在於集合中，則表示目前子字串中的重複字元
                    charSet.remove(s.charAt(left));  //將left指針向前移動，從集合中刪除字符，直到重複字符不再存在
                    left++;
                }
                charSet.add(s.charAt(right)); //將當前字元插入集合並繼續迭代
            }
        }

        return maxLength;
    }
}
