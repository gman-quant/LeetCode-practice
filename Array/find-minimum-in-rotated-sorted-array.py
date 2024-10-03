from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
        Finds the minimum element in a rotated sorted array.

        Args:
            nums (List[int]): List of integers representing the rotated sorted array.

        Returns:
            int: The minimum element in the array.
        """
        p1, p2 = 0, len(nums) - 1  # Initialize pointers for binary search

        while p1 <= p2:
            m = (p1 + p2) // 2  # Calculate the middle index

            # If the middle element equals the last element, we found the minimum
            if nums[m] == nums[p2]:
                return nums[m]
            # If the middle element is greater than the last element,
            # the minimum must be in the right half
            if nums[m] > nums[p2]:
                p1 = m + 1
            else:
                # If the middle element is less than or equal to the last element,
                # the minimum must be in the left half (including the middle)
                p2 = m

        # The minimum element found at the start pointer after loop ends
        return nums[p1]


# Example usage
nums = [4, 5, 6, 7, 0, 1, 2]
solution = Solution()
result = solution.findMin(nums)

# Display the result
print(f"Numbers: {nums}")
print(f"Minimum Element: {result}")
