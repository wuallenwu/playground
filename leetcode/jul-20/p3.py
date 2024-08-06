# 100360. Maximum Number of Operations to Move Ones to the End
# Medium
# You are given a
# binary string
#  s.

# You can perform the following operation on the string any number of times:

# Choose any index i from the string where i + 1 < s.length such that s[i] == '1' and s[i + 1] == '0'.
# Move the character s[i] to the right until it reaches the end of the string or another '1'. For example, for s = "010010", if we choose i = 1, the resulting string will be s = "000110".
# Return the maximum number of operations that you can perform.


# Example 1:

# Input: s = "1001101"

# Output: 4

# Explanation:

# We can perform the following operations:

# Choose index i = 0. The resulting string is s = "0011101".
# Choose index i = 4. The resulting string is s = "0011011".
# Choose index i = 3. The resulting string is s = "0010111".
# Choose index i = 2. The resulting string is s = "0001111".
# Example 2:

# Input: s = "00111"

# Output: 0


class Solution(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        cur = 0
        bonus = 0
        onOne = False
        for i in range(len(s)):
            if onOne:
                if s[i] == "1":
                    bonus += 1
                else:
                    onOne = False
                    count += bonus
                    # print(bonus)
            else:
                if s[i] == "1":
                    onOne = True
                    bonus += 1
        return count


class SolutionSlow(object):
    def maxOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        bonus = 0
        while "10" in s:
            # print(bonus)
            # print(s)
            # start moving things starting toward the end of s
            i = s.find("10")
            # find index of next 1
            for j in range(i + 1, len(s)):
                if s[j] == "1":
                    break
            else:
                j = len(s)
            # move i, and all 1s directly to the right of i to j
            # first get substring of "1"s next to i
            c = bonus
            for k in range(i, -1, -1):
                if s[k] == "1":
                    c += 1
                else:
                    break
            bonus = c
            # toss out everything before j
            s = s[j:]
            count += c

            # now move this whole substring
            # if i - c + 1 <= 0:
            #     print(i)
            #     print(c)
            #     print(s)
            #     print(s[: i - c + 1], s[i + 1 : j], "1" * c, s[j:])
            #     raise
            # s = s[: i - c + 1] + s[i + 1 : j] + "1" * c + s[j:]
            # count += c
        return count


# Main for testing
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxOperations("110100110"))  # 13
    print(solution.maxOperations("00111"))  # 0
    print(solution.maxOperations("1001101"))  # 4
    print(SolutionSlow().maxOperations("110100110"))  # 13
    print(SolutionSlow().maxOperations("00111"))  # 0
    print(SolutionSlow().maxOperations("1001101"))  # 4
