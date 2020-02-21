class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # 运用前缀和的思路来解决这个问题
        outputs = []
        p = [0]
        for i in range(0, len(arr)):
            p.append(p[-1] ^ arr[i])
        for query in queries:
            left, right = query
            output = p[left] ^ p[right+1]
            outputs.append(output)
        return outputs
