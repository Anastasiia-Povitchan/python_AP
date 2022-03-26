class Counter:
    current = 0

    def __init__(self, mini=0, maxi=100):
        self.mini = mini
        self.maxi = maxi

    def adding(self):
        self.current += 1
        if self.current > self.maxi:
            print(self.current, "is out of range. Max value = 100. Counter stop.")
            exit()
            return self.current


if __name__ == '__main__':
    counter = Counter()
    for _ in range(0, 25):
        counter.adding()
        print(counter.current)
    print("Current position:", counter.current)
