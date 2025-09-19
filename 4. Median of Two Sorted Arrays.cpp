class Solution {
public:
    double findMedianSortedArrays(vector<int>& A, vector<int>& B) {
        int na = int(A.size()), nb = int(B.size());  //取得陣列 A 和 B 的長度，分別賦值給變數 na 和 nb
        int n = na + nb;    //計算合併後陣列的總長度

        //檢查總長度 n 是奇數還是偶數
        if (n % 2) {   //若是奇數

            //如果 n 是奇數，中位數就是第 n // 2 個元素（因為索引從 0 開始），
            //只需要呼叫 solve 一次來找出這個元素
            return solve(A, B, n / 2, 0, na - 1, 0, nb - 1);

        } else {   //若是偶數

            //中位數是第 n // 2 - 1 個元素和第 n // 2 個元素的平均值，
            //所以需要呼叫 solve 兩次來找出這兩個元素，然後求它們的平均數
            return 1.0 *
                   (solve(A, B, n / 2 - 1, 0, na - 1, 0, nb - 1) +
                    solve(A, B, n / 2, 0, na - 1, 0, nb - 1)) /
                   2;
        }
    }

    //定義一個遞迴的輔助函式 solve
    //這個函式用來尋找合併後排序陣列中的第 k 小的元素（從索引 0 開始計算）
    int solve(vector<int>& A, vector<int>& B, int k, int aStart, int aEnd,
              int bStart, int bEnd) {
        
        // 如果陣列 A 的搜尋範圍變空了，表示第 k 小的元素一定在陣列 B 中，且位於索引 k - a_start 的位置
        if (aEnd < aStart) {
            return B[k - aStart];
        }

        //如果陣列 B 的搜尋範圍變空了，表示第 k 小的元素一定在陣列 A 中，且位於索引 k - b_start 的位置
        if (bEnd < bStart) {
            return A[k - bStart];
        }

        //取得當前搜尋範圍的中間索引
        int aIndex = (aStart + aEnd) / 2, bIndex = (bStart + bEnd) / 2;
        //取得中間索引處的值
        int aValue = A[aIndex], bValue = B[bIndex];

        //比較兩個中間索引的和與目標索引 k 的關係
        //這意味著目標元素在 A 和 B 的中點之後。換句話說，我們要找的元素肯定在它們的右半部分
        if (aIndex + bIndex < k) {

            //如果 A 的中間值比 B 的大，表示 B 的左半部分的所有元素都比 a_value 小。
            //既然我們要找的是第 k 小的元素，那 B 的左半部分以及 b_value 本身都可以被排除
            //因此，我們在 B 中從 b_index + 1 開始繼續尋找
            if (aValue > bValue) {
                return solve(A, B, k, aStart, aEnd, bIndex + 1, bEnd);

            //如果 B 的中間值比 A 的大，
            //就排除 A 的左半部分，在 A 中從 a_index + 1 開始繼續尋找
            } else {
                return solve(A, B, k, aIndex + 1, aEnd, bStart, bEnd);
            }
        }
        
        //這意味著目標元素在 A 和 B 的中點之前或就是中點。
        //換句話說，我們要找的元素肯定在它們的左半部分
        else {

            //如果 A 的中間值大於 B 的，表示我們要找的元素可能在 B 的右半部分，
            //但絕對不會在 A 的右半部分（從 a_index 到 a_end）
            //因為 a_value 比 b_value 大，而我們只需要尋找 k 之前的元素，
            //所以排除 A 的右半部分，在 A 中從 a_start 到 a_index - 1 繼續尋找
            if (aValue > bValue) {
                return solve(A, B, k, aStart, aIndex - 1, bStart, bEnd);

            //排除 B 的右半部分，在 B 中從 b_start 到 b_index - 1 繼續尋找
            } else {
                return solve(A, B, k, aStart, aEnd, bStart, bIndex - 1);
            }
        }
        return -1;
    }
};
