class Counter:
    def __init__(self):
        # use a fixed sized list to store all count
        # for every element of the list, it is a pair that
        # indicates [hit_timestamp, hit_count]
        # I think it is necessary to store the hit timestamp
        # because we always for 301 time stamp, and 601 time stamp,
        # they will both map to index 1
        self.count = [[0, 0] for i in range(300)]

    def Hit(self, timestamp):
        # once we call hit for the timestamp, we need to first
        # judge whether the timestamp we stored at timestamp % 300 pos
        # is same as the current timestamp. If it is we add count, else we reset the count
        if timestamp == self.count[timestamp % 300][0]:
            self.count[timestamp % 300][1] += 1
        else:
            self.count[timestamp % 300][0] = timestamp
            self.count[timestamp % 300][1] = 1

    def GetHitCount(self, timestamp):
        # when get hit count, we need to judge whether our current
        # timestamp is actually no less than 300s later than the stored timestamp
        # if it is, we add on to the answer,
        # else, we do not add to the answer
        ans = 0
        for count_timestamp, hit_count in self.count:
            if count_timestamp > timestamp - 300:
                ans += hit_count
        return ans


def main():
    counter = Counter()
    # queue_time_stamps = [301]
    counter.Hit(1)
    counter.Hit(2)
    counter.Hit(2)
    # return len(queue_time) = 3
    # queue_time_stamps = [1, 2, 2]
    print(counter.GetHitCount(4))

    # [1, 2, 2, 300]
    counter.Hit(300)

    # len(queue) = 4
    print(counter.GetHitCount(300))
    # [2, 2, 300] = 3
    print(counter.GetHitCount(301))


if __name__ == '__main__':
    main()
