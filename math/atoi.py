class Solution:
    # @param str: a string
    # @return an integer
    def atoi(self, str):
        # write your code here
        pointer = 0
        isNegative = False
        str = str.strip()
        length = len(str)
        if pointer == length:
            return 0
        if str[pointer] == '-':
            isNegative = True
            pointer += 1
        elif str[pointer] == '+':
            isNegative = False
            pointer += 1
        solution = 0
        for pointer in range(pointer, length):
            if not str[pointer].isdigit():
                break
            else:
                solution *= 10
                solution += int(str[pointer])
        if not isNegative and solution > 2147483647:
            return 2147483647
        elif isNegative and solution > 2147483647:
            return -2147483648
        if isNegative:
            return -1 * solution
        else:
            return solution