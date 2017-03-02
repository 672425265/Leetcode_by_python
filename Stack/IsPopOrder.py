class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if len(pushV) == 0:
            return False
        stack = []
        i = 0
        j = 0
        while i < len(pushV):
            stack.append(pushV[i])
            i += 1
            while j < len(popV) and stack[-1] == popV[j]:
                stack.pop()
                j += 1
        return len(stack) == 0