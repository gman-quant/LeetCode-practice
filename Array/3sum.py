from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        https://leetcode.com/problems/3sum/
        Finds all unique triplets in the array that sum up to zero.

        Args:
            nums (List[int]): List of integers to search for triplets.

        Returns:
            List[List[int]]: A list of unique triplets that sum to zero.
        """
        triplets_array = []  # Initialize the list to store unique triplets

        nums.sort()  # Sort the array to facilitate the two-pointer approach
        n = len(nums)

        for i in range(n - 2):  # Iterate through the array up to the third last element

            # Skip duplicate elements to avoid duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            complement = -nums[i]  # Calculate the required complement for the current element
            visited = set()  # Track visited numbers to avoid duplicates

            j, k = i + 1, n - 1  # Initialize two pointers for the remaining part of the array

            while j < k:
                two_sum = nums[j] + nums[k]  # Calculate the sum of the two pointers

                if two_sum == complement:  # Found a triplet
                    if nums[j] in visited:  # Skip if we've already used this number
                        j += 1
                        k -= 1
                        continue
                    visited.add(nums[j])  # Add the number to the visited set
                    triplets_array.append([nums[i], nums[j], nums[k]])  # Add the triplet to the result

                elif two_sum > complement:  # Sum is too high, move the right pointer
                    k -= 1
                else:  # Sum is too low, move the left pointer
                    j += 1

        return triplets_array


# Example usage
nums = [-1, 0, 1, 2, -1, -4]
solution = Solution()
result = solution.threeSum(nums)

# Display the result
print(f"Numbers: {nums}")
print(f"Unique Triplets that Sum to Zero: {result}")
