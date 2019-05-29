class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        import copy
        if len(nums) <=3:
            return []
        if len(nums) == 4:
            return [nums] if sum(nums) == target else []
        triplets=[]
        pre_list_set = set()
        
        def search(seq, t):
            # if len(seq) <= 2
            #     return t in seq
            left = 0
            right = len(seq) - 1
            if seq[left] == t or seq[right] == t:
                return True
            while left < right:
                mid = (left + right) / 2
                if seq[mid] == t:
                    return True
                elif seq[mid] > t:
                    right = mid
                else:
                    if left == mid:
                        break
                    left = mid
            return False
        
        def findTriplets(pre_nums,sub_nums):
            pre_tuple = ','.join([str(p) for p in pre_nums])
            if pre_tuple in pre_list_set:
                return
            pre_list_set.add(pre_tuple)
            if len(pre_nums) == 3:
                sum_pre_nums = sum(pre_nums)
                if len(sub_nums) > 0 and sum_pre_nums + sub_nums[-1] < target:
                    return
                last_num = target - sum_pre_nums
                if search(sub_nums, last_num):
                    triplets.append(tuple(pre_nums + [last_num]))
                # for num in sub_nums:
                #     tmp_sum = num + sum_pre_nums
                #     if tmp_sum == target:
                #         tmp = copy.copy(pre_nums)
                #         tmp.append(num)
                #         triplets.append(tuple(tmp))
                #     elif tmp_sum > target:
                #         break
                return
            for i in range(len(sub_nums)-1):
                tmp = copy.copy(pre_nums)
                tmp.append(sub_nums[i])                
                findTriplets(tmp, sub_nums[i+1:])
        findTriplets([], nums)
        return list(set(triplets))
