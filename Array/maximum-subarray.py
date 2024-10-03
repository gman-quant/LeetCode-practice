from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/maximum-subarray/
        Finds the contiguous subarray within a one-dimensional array of numbers
        that has the largest sum.

        Args:
            nums (List[int]): List of integers representing the array.

        Returns:
            int: Maximum sum of the contiguous subarray.
        """
        max_sum = float('-inf')  # Initialize max_sum to the smallest possible value
        current_sum = 0  # Initialize the current sum to 0

        for number in nums:
            # Update current_sum: either add the current number or start a new subarray
            current_sum = max(current_sum + number, number)
            # Update max_sum if the current_sum is greater
            max_sum = max(max_sum, current_sum)

        return max_sum


# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
solution = Solution()
result = solution.maxSubArray(nums)

# Display the result
print(f"Numbers: {nums}")
print(f"Maximum Subarray Sum: {result}")
