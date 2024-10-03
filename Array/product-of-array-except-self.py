from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/product-of-array-except-self/
        Returns an array such that output[i] is equal to the product of all the numbers
        in the input array except nums[i].

        Args:
            nums (List[int]): List of integers to process.

        Returns:
            List[int]: Array with products of all elements except self.
        """
        n = len(nums)
        product_array = [1] * n  # Initialize the result array

        # Build prefix products in the result array
        prefix_product = 1
        for i in range(n):
            product_array[i] = prefix_product
            prefix_product *= nums[i]  # Update prefix product for next index

        # Multiply suffix products to the result array
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            product_array[i] *= suffix_product  # Multiply with current suffix product
            suffix_product *= nums[i]  # Update suffix product for next index

        return product_array


# Example usage
nums = [1, 2, 3, 4]
solution = Solution()
result = solution.productExceptSelf(nums)

# Display the result
print(f"Numbers: {nums}")
print(f"Product Except Self: {result}")
