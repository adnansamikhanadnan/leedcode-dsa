class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digits = str(n)
        sign = 1
        total = 0

        for d in digits:
            total += sign * int (d)
            sign *= -1

        return total
        