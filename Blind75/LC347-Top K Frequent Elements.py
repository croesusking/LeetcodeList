class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #LC 347 - Top K frequent elements

        if len(nums)==k:
            return nums
        

        count = Counter(nums)
        res = []
        count0 = [[-c,k] for k,c in count.items()]
        heapq.heapify(count0)

        for i in range(k):
            res.append(heapq.heappop(count0)[1])

        return res

