class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        stored_color = {}
        res = 0
        for i in range(len(colors)):
            for c in stored_color:
                if c == colors[i]:
                    continue
                res = max(i - stored_color[c], res)
            if colors[i] not in stored_color:
                stored_color[colors[i]] = i
        return res
