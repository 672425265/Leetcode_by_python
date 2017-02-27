
class Solution(object):
    stackPush = []
    stackPop = []

    def push(self, node):
        stackPush = self.stackPush
        stackPush.append(node)

    def pop(self):
        stackPush = self.stackPush
        stackPop = self.stackPop
        if len(stackPush) == 0 and len(stackPop) == 0:
            return None
        elif len(stackPop) == 0:
            while len(stackPush) != 0:
                stackPop.append(stackPush.pop())
        return stackPop.pop()