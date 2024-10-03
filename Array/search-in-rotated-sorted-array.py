from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        https://leetcode.com/problems/search-in-rotated-sorted-array/
        Searches for a target value in a rotated sorted array.

        Args:
            nums (List[int]): List of integers representing the rotated sorted array.
            target (int): The value to search for in the array.

        Returns:
            int: The index of the target value if found, otherwise -1.
        """
        p1, p2 = 0, len(nums) - 1  # Initialize pointers for binary search

        while p1 <= p2:
            m = (p1 + p2) // 2  # Calculate the middle index

            # Check if the middle element is the target
            if nums[m] == target:
                return m

            # Determine which half is sorted
            if nums[m] < nums[p2]:  # Right half is sorted
                # Check if target is in the sorted right half
                if nums[m] < target <= nums[p2]:
                    p1 = m + 1  # Search in the right half
                else:
                    p2 = m - 1  # Search in the left half
            else:  # Left half is sorted
                # Check if target is in the sorted left half
                if nums[p1] <= target < nums[m]:
                    p2 = m - 1  # Search in the left half
                else:
                    p1 = m + 1  # Search in the right half

        return -1  # Target not found


# Example usage
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
solution = Solution()
result = solution.search(nums, target)

# Display the result
print(f"Numbers: {nums}")
print(f"Target: {target}")
print(f"Index of Target: {result}")
