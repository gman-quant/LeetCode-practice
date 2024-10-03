class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        https://leetcode.com/problems/sum-of-two-integers/
        Computes the sum of two integers without using the + operator.

        Args:
            a (int): The first integer.
            b (int): The second integer.

        Returns:
            int: The sum of the two integers.
        """
        MASK = 0xFFF  # Mask to keep only the last 12 bits
        MAX_INT = 0x7FF  # Maximum positive integer for 12 bits

        while b != 0:  # Continue until there is no carry
            # Calculate the sum without carry
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        # Handle overflow for 12-bit signed integers
        return a if a <= MAX_INT else ~(a ^ MASK)


# Example usage
a = 1
b = 2
solution = Solution()
result = solution.getSum(a, b)

# Display the result
print(f"Sum of {a} and {b}: {result}")
