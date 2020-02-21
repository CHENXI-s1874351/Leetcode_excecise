class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        arr = [(0, 0)]
        x_, y_ = 0, 0
        for c in command:
            if c =='U':
                y_ += 1
                arr.append((x_, y_))
            else:
                x_ += 1
                arr.append((x_, y_))
        
        def pointVisited(arr, x, y, point):
            k = min(point[0] // x, point[1] // y)
            x_ = point[0] - x * k
            y_ = point[1] - y * k
            if (x_, y_) in arr:
                return True
            else:
                return False

        for obstacle in obstacles:
            if pointVisited(arr, x_, y_, obstacle):
                if obstacle[0] < x and obstacle[1] <= y:
                    return False
                elif obstacle[0] <= x and obstacle[1] < y:
                    return False
        
        if pointVisited(arr, x_, y_, (x,y)): return True
        else: return False



