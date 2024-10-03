from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/maximum-product-subarray/
        Calculates the maximum product of a contiguous subarray.

        Args:
            nums (List[int]): List of integers representing the array.

        Returns:
            int: Maximum product of any contiguous subarray.
        """
        # Initialize the largest, minimum, and maximum product to the first element
        largest_product = min_product = max_product = nums[0]

        for i in range(1, len(nums)):
            # Swap min and max if the current number is negative
            if nums[i] < 0:
                min_product, max_product = max_product, min_product

            # Update the min and max products for the current number
            min_product = min(min_product * nums[i], nums[i])
            max_product = max(max_product * nums[i], nums[i])

            # Update the largest product found so far
            largest_product = max(largest_product, max_product)

        return largest_product


# Example usage
nums = [2, 3, -2, 4]
solution = Solution()
result = solution.maxProduct(nums)

# Display the result
print(f"Numbers: {nums}")
print(f"Maximum Product Subarray: {result}")
