class Solution:
    def smallestNumber(self, num: int) -> int:
        l = str(num)
        l = list(l)
        flag = 1
        if num < 0:
            flag = -1
            l = [int(i) for i in l[1:]]
            l.sort( reverse = True)
            res = "".join(str(i) for i in l)
        elif num > 0:
            l = [int(i) for i in l]
            l.sort()
            res = ''
            n = l.count(0)
            s = "".join(str(i) for i in l)
            s_1 = s[n:]
            res += s_1[0] + '0' * n + s_1[1:]
        else:
            return 0
        return int(res) * flag
