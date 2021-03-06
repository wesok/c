# 暴力法
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        sl = list(s)
        
        for i in range(0, len(sl), 2 * k):
            # py自带的类，reversed： 返回一个把序列之翻转后的迭代器
            sl[i : i + k] = reversed(sl[i : i + k])
            
            # # 也可以写成这种形式    
            # sl[i : i + k] = sl[i : i + k][::-1]
        
        return "".join(sl)  