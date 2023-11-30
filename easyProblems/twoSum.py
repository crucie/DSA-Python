class Solution(object):
    def twoSum(self, nums, target):
        # Create a dictionary to store the elements and their indices
        num_dict = {}

        for i, num in enumerate(nums):
            # Check if the complement (target - num) is in the dictionary
            complement = target - num
            if complement in num_dict:
                # Return the indices of the two numbers
                return [num_dict[complement], i]

            # Add the current number and its index to the dictionary
            num_dict[num] = i

        # If no solution is found, return an empty list or raise an exception
        raise ValueError("No solution found")

# Example usage:
nums = [2, 7, 11, 15]
target = 9

# Create an instance of the Solution class
solution = Solution()

# Call the twoSum method to find the result
result = solution.twoSum(nums, target)
print(result)