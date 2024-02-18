class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)

        cnt_b = [0] * n

        for i, blk in enumerate(blocks):
            if i > 0:
                cnt_b[i] += cnt_b[i-1]
            cnt_b[i] += int(blk == "B")
        
        min_fill = float("inf")

        for j in range(n-k+1):
            prev = 0 if j == 0 else cnt_b[j-1]

            cur_num = cnt_b[j+k-1] - prev

            min_fill = min(min_fill, k - cur_num)

        return min_fill