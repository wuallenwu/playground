# 100329. Minimum Operations to Make Array Equal to Target
# Hard
# You are given two positive integer arrays nums and target, of the same length.

# In a single operation, you can select any
# subarray
#  of nums and increment or decrement each element within that subarray by 1.

# Return the minimum number of operations required to make nums equal to the array target.


# Example 1:

# Input: nums = [3,5,1,2], target = [4,6,2,4]

# Output: 2

# Explanation:

# We will perform the following operations to make nums equal to target:
# - Increment nums[0..3] by 1, nums = [4,6,2,3].
# - Increment nums[3..3] by 1, nums = [4,6,2,4].

# Example 2:

# Input: nums = [1,3,2], target = [2,1,4]

# Output: 5

# Explanation:

# We will perform the following operations to make nums equal to target:
# - Increment nums[0..0] by 1, nums = [2,3,2].
# - Decrement nums[1..1] by 1, nums = [2,2,2].
# - Decrement nums[1..1] by 1, nums = [2,1,2].
# - Increment nums[2..2] by 1, nums = [2,1,3].
# - Increment nums[2..2] by 1, nums = [2,1,4].


class Solution(object):
    def minimumOperations(self, nums, target):
        """
        :type nums: List[int]
        :type target: List[int]
        :rtype: int
        """
        # Get array of deltas from nums to target
        deltas = [target[i] - nums[i] for i in range(len(nums))]
        # Create dp

        # Iterate through deltas
        # If delta is positive, increment all elements in nums up to target by delta
        # If delta is negative, decrement all elements in nums up to target by delta
        # If delta is 0, do nothing
        # Increment counter
        # Return counter
        count = 0
        for i in range(len(deltas)):
            if deltas[i] > 0:
                for j in range(i, len(nums)):
                    nums[j] += deltas[i]
                count += 1
            elif deltas[i] < 0:
                for j in range(i, len(nums)):
                    nums[j] += deltas[i]
                count += 1
        return count


# Main for testing
if __name__ == "__main__":
    print(Solution().minimumOperations([3, 5, 1, 2], [4, 6, 2, 4]))  # 2
    print(Solution().minimumOperations([1, 3, 2], [2, 1, 4]))  # 5
