class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        n,m = len(matrix),len(matrix[0])
        for row in matrix:
            for c in range(1,m):
                row[c] += row[c-1]
        answer = 0
        for c1 in range(m):
            for c2 in range(c1,m):
                total = 0
                freq = {0:1}
                for row in matrix:
                    total += row[c2] - (row[c1-1] if c1 else 0)
                    answer += freq.get(total-target,0)
                    freq[total] = freq.get(total,0)+1 
        return answer