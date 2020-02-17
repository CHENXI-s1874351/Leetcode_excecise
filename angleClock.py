class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = (60 - minutes) * 6
        hour_angle = (12 - hour) * 30 - minutes * 0.5
        answer = minute_angle - hour_angle
        if answer <= -180: return 360 + answer
        elif answer > -180 and answer < 0: return -answer
        elif answer < 180 and answer >= 0: return answer
        else: return 360 - answer
