# 100372. Number of Bit Changes to Make Two Integers Equal
# Easy
# You are given two positive integers n and k.

# You can choose any bit in the binary representation of n that is equal to 1 and change it to 0.

# Return the number of changes needed to make n equal to k. If it is impossible, return -1.


# Example 1:

# Input: n = 13, k = 4

# Output: 2

# Explanation:
# Initially, the binary representations of n and k are n = (1101)2 and k = (0100)2.
# We can change the first and fourth bits of n. The resulting integer is n = (0100)2 = k.

# Example 2:

# Input: n = 21, k = 21

# Output: 0

# Explanation:
# n and k are already equal, so no changes are needed.

# Example 3:

# Input: n = 14, k = 13

# Output: -1

# Explanation:
# It is not possible to make n equal to k.


class Solution(object):
    def minChanges(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # Get binary representation of n and k
        n_bin = bin(n)
        k_bin = bin(k)
        # Remove "0b" at front
        n_bin = n_bin[2:]
        k_bin = k_bin[2:]
        if len(n_bin) > len(k_bin):
            # pad k_bin with zeroes at front
            k_bin = "0" * (len(n_bin) - len(k_bin)) + k_bin
        elif len(n_bin) < len(k_bin):
            # pad n_bin with zeroes at front
            n_bin = "0" * (len(k_bin) - len(n_bin)) + n_bin
        # Compare two strings and see if we can turn 1 in n_bin to 0
        count = 0
        for i in range(len(n_bin)):
            if n_bin[i] == "1" and k_bin[i] == "0":
                count += 1
            elif n_bin[i] == "0" and k_bin[i] == "1":
                return -1
        return count


# main for testing
if __name__ == "__main__":
    print(Solution().minChanges(13, 4))  # 2
    print(Solution().minChanges(21, 21))  # 0
    print(Solution().minChanges(14, 13))  # -1
