class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        https://leetcode.com/problems/number-of-1-bits/
        Counts the number of 1 bits (Hamming weight) in the binary representation
        of a non-negative integer.

        Args:
            n (int): The non-negative integer whose 1 bits are to be counted.

        Returns:
            int: The number of 1 bits in the binary representation of n.
        """
        count = 0  # Initialize count of 1 bits to zero

        while n:  # Continue until all bits are processed
            count += n & 1  # Add 1 to count if the least significant bit is 1
            n >>= 1  # Right shift n to process the next bit

        return count  # Return the total count of 1 bits


# Example usage
n = 11  # Binary representation: 1011
solution = Solution()
result = solution.hammingWeight(n)

# Display the result
print(f"Number: {n}")
print(f"Hamming Weight (Number of 1 bits): {result}")
