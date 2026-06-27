class TimeWindowCounter:
    def __init__(self, duration):
        self.duration = duration
        self.hits = []

    def record_hit(self, timestamp):
        self.hits.append(timestamp)
        self.clean_old(timestamp)
        return len(self.hits)

    def clean_old(self, current_time):
        while self.hits and self.hits[0] <= current_time - self.duration:
            self.hits.pop(0)

counter = TimeWindowCounter(300)
counter.record_hit(100)
counter.record_hit(200)
print(counter.record_hit(450))