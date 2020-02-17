class TweetCounts:

    def __init__(self):
        self.d = {}
        
    def recordTweet(self, tweetName, time):
        if tweetName in self.d:
            if time <= self.d[tweetName][0]: 
                self.d[tweetName].insert(0, time)
                return
            flag = False
            for i in range(0, len(self.d[tweetName])-1):
                if self.d[tweetName][i] <= time and self.d[tweetName][i+1] >= time:
                    flag = True
                    break
            if flag:
                self.d[tweetName].insert(i+1, time)
            else:
                self.d[tweetName].append(time)                
        else:
            self.d[tweetName] = [time]
        
    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        if tweetName not in self.d:
            return None
        times = self.d[tweetName]
        if freq == 'minute': interval = 60
        elif freq == 'hour': interval = 3600
        else: interval = 3600*24
        index = startTime
        outputs = []
        count = 0
        for time in times:
            if time > endTime:
                break
            if time < index: continue
            elif time >= index and time < (index + interval):
                count += 1
            elif time >= (index + interval):
                outputs.append(count)
                count = 1
                zeros = 0
                while time >= (index + interval):
                    index += interval
                    zeros += 1
                for i in range(zeros-1):
                    outputs.append(0)
        outputs.append(count)
        zeros = 0
        while index <= endTime:
            zeros += 1
            index += interval
        for i in range(zeros-1):
            outputs.append(0)

        return outputs



# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)