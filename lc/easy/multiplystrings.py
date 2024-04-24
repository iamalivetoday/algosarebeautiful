#LC 43
#Given two non-negative integers num1 and num2 represented as strings, 
# return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def multiply(self, num1, num2):
        # Convert strings to integers
        num1_int = self.stringToTotalNum(num1)
        num2_int = self.stringToTotalNum(num2)

        # Perform multiplication
        result = num1_int * num2_int

        # Convert the result back to a string and return
        return str(result)

    def stringToTotalNum(self, s):
        total = 0
        i = 0
        for ch in s[::-1]:
            digit = self.charToOneNum(ch)
            total += digit * (10 ** i)
            i += 1
        return total

    def charToOneNum(self, s):
        return ord(s) - ord('0')  # A more concise way to convert char to int

