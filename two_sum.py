# Solution1(Time:O(n^2), Space:O(1))
# def two_sum(nums, target):
#    for i in range(len(nums) - 1):
#        for j in range(i + 1, len(nums)):
#            if nums[i] + nums[j] == target:
#                return [i, j]
# Solution1(Time:O(n), Space:O(n))
def two_sum(nums, target):
    dict_pair_location = {}
    for i in range(len(nums)):
        if nums[i] in dict_pair_location:
            return [dict_pair_location[nums[i]], i]
        else:
            dict_pair_location[target - nums[i]] = i
