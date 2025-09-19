class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        na, nb = len(A), len(B) #取得陣列 A 和 B 的長度，分別賦值給變數 na 和 nb
        n = na + nb             #計算合併後陣列的總長度


        #定義一個遞迴的輔助函式 solve
        #這個函式用來尋找合併後排序陣列中的第 k 小的元素（從索引 0 開始計算）
        def solve(k, a_start, a_end, b_start, b_end):
            
            #如果陣列 A 的搜尋範圍變空了，表示第 k 小的元素一定在陣列 B 中，且位於索引 k - a_start 的位置
            if a_start > a_end:
                return B[k - a_start]
            
            #如果陣列 B 的搜尋範圍變空了，表示第 k 小的元素一定在陣列 A 中，且位於索引 k - b_start 的位置
            if b_start > b_end:
                return A[k - b_start]

            #取得當前搜尋範圍的中間索引
            a_index, b_index = (a_start + a_end) // 2, (b_start + b_end) // 2
            #取得中間索引處的值
            a_value, b_value = A[a_index], B[b_index]

            #比較兩個中間索引的和與目標索引 k 的關係
            #這意味著目標元素在 A 和 B 的中點之後。換句話說，我們要找的元素肯定在它們的右半部分
            if a_index + b_index < k:
                
                #如果 A 的中間值比 B 的大，表示 B 的左半部分的所有元素都比 a_value 小。
                #既然我們要找的是第 k 小的元素，那 B 的左半部分以及 b_value 本身都可以被排除
                #因此，我們在 B 中從 b_index + 1 開始繼續尋找
                if a_value > b_value:
                    return solve(k, a_start, a_end, b_index + 1, b_end)

                #如果 B 的中間值比 A 的大，
                #就排除 A 的左半部分，在 A 中從 a_index + 1 開始繼續尋找
                else:
                    return solve(k, a_index + 1, a_end, b_start, b_end)
            
            #這意味著目標元素在 A 和 B 的中點之前或就是中點。
            #換句話說，我們要找的元素肯定在它們的左半部分
            else:

                #如果 A 的中間值大於 B 的，表示我們要找的元素可能在 B 的右半部分，
                #但絕對不會在 A 的右半部分（從 a_index 到 a_end）
                #因為 a_value 比 b_value 大，而我們只需要尋找 k 之前的元素，
                #所以排除 A 的右半部分，在 A 中從 a_start 到 a_index - 1 繼續尋找
                if a_value > b_value:
                    return solve(k, a_start, a_index - 1, b_start, b_end)

                #排除 B 的右半部分，在 B 中從 b_start 到 b_index - 1 繼續尋找
                else:
                    return solve(k, a_start, a_end, b_start, b_index - 1)


        #檢查總長度 n 是奇數還是偶數
        if n % 2:   #若是奇數

            #如果 n 是奇數，中位數就是第 n // 2 個元素（因為索引從 0 開始），
            #只需要呼叫 solve 一次來找出這個元素
            return solve(n // 2, 0, na - 1, 0, nb - 1)

        else:    #若是偶數

            # 中位數是第 n // 2 - 1 個元素和第 n // 2 個元素的平均值，
            #所以需要呼叫 solve 兩次來找出這兩個元素，然後求它們的平均數
            return (
                solve(n // 2 - 1, 0, na - 1, 0, nb - 1)
                + solve(n // 2, 0, na - 1, 0, nb - 1)
            ) / 2
