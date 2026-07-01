class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        #建立一個假頭節點。這個節點本身不包含在最終結果中，只作為新鏈結串列的起點
        dummyHead = ListNode(0)
        #tail 是一個尾部指針，始終指向結果鏈結串列的最後一個節點，方便我們連接新節點
        tail = dummyHead
        #初始化進位變數，用於儲存相加後可能產生的進位
        carry = 0

        #迴圈會持續執行，直到兩個輸入鏈結串列都遍歷完畢（l1 和 l2 都為 None），且進位變數 carry 為 0
        while l1 is not None or l2 is not None or carry != 0:

            #使用條件表達式，如果 l1 存在，則取它的值；否則取 0。l2 同上
            #這優雅地處理了兩個鏈結串列長度不一致的情況
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

           
            sum = digit1 + digit2 + carry  #將兩個數字和當前進位全部相加
            digit = sum % 10               #計算當前節點應該放的數字（個位數）
            carry = sum // 10              #計算新的進位

            #構建結果鏈結串列
            newNode = ListNode(digit)  #根據計算出的 digit 創建一個新節點
            tail.next = newNode        #將新節點連接到結果鏈結串列的尾部
            tail = tail.next           #將 tail 指針前移，使其指向新加入的節點，為下一次循環做準備

            #前進到下一個節點
            #將 l1 指針前移到下一個節點。如果 l1 已經是 None，則保持為 None。l2 也是一樣的處理方式
            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        #返回結果
        result = dummyHead.next  #迴圈結束後，dummyHead 的下一個節點就是我們結果鏈結串列的開頭
        dummyHead.next = None    #這一步不是必須的，但可以斷開 dummyHead 與結果鏈結串列的連接，釋放記憶體
        return result            #返回最終的結果鏈結串列
