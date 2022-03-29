class Counter:

    def __init__(self, mini=0, maxi=100, current=0):
        self.mini = mini
        self.maxi = maxi
        self.current = current

    def adding(self):
        self.current += 1
        if self.current > self.maxi:
            raise AssertionError('Current position > 100')


if __name__ == '__main__':
    counter = Counter()
    for _ in range(105):
        counter.adding()
        print(counter.current)
    print("Current position:", counter.current)
