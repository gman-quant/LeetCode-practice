from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        https://leetcode.com/problems/container-with-most-water/
        Calculates the maximum area of water that can be contained
        between two vertical lines.

        Args:
            height (List[int]): List of integers representing the heights
                                 of the vertical lines.

        Returns:
            int: The maximum area of water that can be contained.
        """
        max_amount = 0  # Initialize the maximum area to zero

        p1, p2 = 0, len(height) - 1  # Initialize two pointers at the start and end

        while p1 < p2:  # Continue until the two pointers meet
            # Calculate the current area formed by the lines at p1 and p2
            current_amount = min(height[p1], height[p2]) * (p2 - p1)
            # Update max_amount if the current area is larger
            max_amount = max(max_amount, current_amount)

            # Move the pointer corresponding to the shorter line inward
            if height[p1] > height[p2]:
                p2 -= 1
            else:
                p1 += 1

        return max_amount  # Return the maximum area found


# Example usage
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
solution = Solution()
result = solution.maxArea(height)

# Display the result
print(f"Heights: {height}")
print(f"Maximum Area: {result}")
