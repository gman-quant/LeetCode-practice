from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        https://leetcode.com/problems/contains-duplicate/
        Checks if the list contains any duplicate values.

        Args:
            nums (List[int]): List of integers to check.

        Returns:
            bool: True if a duplicate is found, False otherwise.
        """
        visited = set()  # Set to store seen numbers
        for n in nums:
            if n in visited:  # If number is already in the set, it's a duplicate
                return True
            visited.add(n)  # Add number to the set
        return False  # No duplicates found


# Example usage
nums = [1, 2, 3, 4, 5, 6, 1]
solution = Solution()
result = solution.containsDuplicate(nums)

# Show the result
print(f"Numbers: {nums}")
print(f"Contains Duplicate: {result}")
