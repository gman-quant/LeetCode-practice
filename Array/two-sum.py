from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/problems/two-sum/description/
        Finds two numbers in 'nums' that add up to the 'target' value.
        Returns their indices.
        """
        # Dictionary to store the required complement of each number and its index.
        complement_map = {}

        # Iterate through each number in the list.
        for index, number in enumerate(nums):
            # Check if the current number is already a complement of a previous number.
            if number in complement_map:
                # If yes, return the indices of the complement and current number.
                return [complement_map[number], index]

            # Otherwise, calculate the complement needed for the current number.
            # Store the complement along with the current index.
            complement_map[target - number] = index


# Example list of numbers and target
nums = [2, 7, 11, 15, 3, 6, 1, 8, 10, 5]
target = 13

# Create an instance of Solution and call the twoSum function
solution = Solution()
result = solution.twoSum(nums, target)

# Show the result
print(f"Numbers: {nums}")
print(f"Target: {target}")
print(f"Result: {result}")  # Output the indices of the two numbers that add up to the target
