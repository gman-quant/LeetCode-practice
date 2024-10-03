from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        https://leetcode.com/problems/counting-bits/
        Computes the number of 1 bits in the binary representation of each number
        from 0 to n.

        Args:
            n (int): The non-negative integer up to which to count the bits.

        Returns:
            List[int]: A list where the ith element is the number of 1 bits in the
                        binary representation of i.
        """
        # Initialize an array to store the number of 1 bits for each number
        num_of_1_bit_array = [0] * (n + 1)

        for i in range(1, n + 1):
            # Use previously computed results: right shift (i >> 1) gives the number
            # of 1 bits for half the number, and (i & 1) adds 1 if the least significant
            # bit of i is 1.
            num_of_1_bit_array[i] = num_of_1_bit_array[i >> 1] + (i & 1)

        return num_of_1_bit_array  # Return the array containing the counts


# Example usage
n = 16
solution = Solution()
result = solution.countBits(n)

# Display the result
print(f"Count of 1 bits from 0 to {n}: {result}")
