class Solution:
    def maxEvents(self,events):
        # 优先安排结束时间早的会议
        events.sort(key=lambda x:x[1])
        visited = set()
        for s,e in events:
            for day in range(s,e+1):
                if day not in visited:
                    visited.add(day)
                    break
        return len(visited)
