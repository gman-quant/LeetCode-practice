from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/missing-number/
        Finds the missing number in a list of numbers from 0 to n.

        Args:
            nums (List[int]): List of n distinct numbers taken from 0, 1, 2, ..., n.

        Returns:
            int: The missing number from the list.
        """
        n = len(nums)  # Get the total count of numbers, which should be n

        # Calculate the expected sum of numbers from 0 to n and subtract the actual sum
        return n * (n + 1) // 2 - sum(nums)

# Example usage
nums = [3, 0, 1]  # Missing number is 2
solution = Solution()
result = solution.missingNumber(nums)

# Display the result
print(f"Numbers: {nums}")
print(f"Missing Number: {result}")
