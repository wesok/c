# https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/bi-jiao-zhi-jie-gao-xiao-de-zuo-fa-han-tu-jie-by-w/
# 迭代法：
# TC：O(n)
# SC: O(1)

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre, pre.next = self, head

        while pre.next and pre.next.next:
            # a,b 指向第一、第二个节点
            a = pre.next
            b = a.next

            pre.next, b.next, a.next = b, a, b.next
            pre = a
        
        return self.next
        
        
        
        
        # # 方法二：交换指针
        # # 添加一个空头指针
        # thead = ListNode(-1)
        # thead.next = head
        # c = thead
        # while c.next and c.next.next:
        #     a, b = c.next, c.next.next
        #     # 空头指向b，方便第一个节点的移动
        #     # a指向第三个node
        #     c.next, a.next = b, b.next
        #     # b指向a，完成前两个的交换
        #     b.next = a
        #     c = c.next.next
        # return thead.next