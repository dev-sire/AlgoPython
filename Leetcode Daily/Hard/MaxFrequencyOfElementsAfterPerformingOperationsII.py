class Solution:
    
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()
        # this part implements yesterday's solution to deal with in-array target values
        arrayValMaxFreq = self.maxFrequencyOfArrayVal(nums, k , numOperations) 

        #sliding window solution assuming every element requires an operation:
        left = 0 
        otherValMaxFreq = 0
        for right in range(len(nums)):
            # we adjust the starting point until the sorted subarray is valid
            while nums[right] > nums[left] + 2*k:
                left += 1
            #recording current window length
            otherValMaxFreq = max(otherValMaxFreq, right - left + 1)
            #if the length exceeds the number of operations, we have reached the longest possible window
            if otherValMaxFreq >= numOperations:
                otherValMaxFreq = numOperations
                break
            
        return max(arrayValMaxFreq, otherValMaxFreq)


    # this is the solution from yesterday's problem, used to solve for the values present in the original array
    def maxFrequencyOfArrayVal(self, nums, k, numOperations):
        # NB: nums is already sorted
        count = Counter(nums)

        maxFreq = 0
        # we enumerate the values existing in the original array and deal with them
        for val in count.keys():
            left = bisect_left(nums, val - k)
            right = bisect_right(nums, val + k) - 1
            freq = min(right - left + 1, numOperations + count[val])
            maxFreq = max(maxFreq, freq)

        return maxFreq

        