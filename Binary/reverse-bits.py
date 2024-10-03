class Solution:
    def reverseBits(self, n: int) -> int:
        """
        https://leetcode.com/problems/reverse-bits/
        Reverses the bits of a given 32-bit unsigned integer.

        Args:
            n (int): The 32-bit unsigned integer to reverse.

        Returns:
            int: The reversed integer as a 32-bit unsigned integer.
        """
        reversed_num = 0  # Initialize the reversed number to zero

        for _ in range(32):  # Process each of the 32 bits
            reversed_num <<= 1  # Shift the reversed number left to make space for the next bit
            reversed_num += n & 1  # Add the least significant bit of n to reversed_num
            n >>= 1  # Shift n right to process the next bit

        return reversed_num  # Return the final reversed number


# Example usage
n = 43261596  # Binary: 00000010100101000001111010011100
solution = Solution()
result = solution.reverseBits(n)

# Display the result
print(f"Original Number: {n}")
print(f"Reversed Bits: {result}")
