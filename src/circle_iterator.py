class CircleIterator:
    def __init__(self, num):
        self.people = range(1, num+1, 1)
        self.wielder = True
        self.even = len(self.people) % 2 == 0
        self.loop = 1

    def reset_odd_or_even(self):
        self.even = len(self.people) % 2 == 0

    def execute(self):
        if self.even and self.wielder:
            print("even + wielder")
            self.loop = self.loop*2
            self.people = range(self.people[0], self.people[-1], self.loop)
            self.reset_odd_or_even()

        elif not self.even and self.wielder:
            print("odd + wielder")
            self.loop = self.loop*2
            self.people = range(self.people[0], self.people[-1] + 1, self.loop)
            self.wielder = False
            self.reset_odd_or_even()

        elif self.even and not self.wielder:
            print("even + not wielder")
            self.loop = self.loop*2
            self.people = range(self.people[1], self.people[-1] + 1, self.loop)
            self.reset_odd_or_even()

        elif not self.even and not self.wielder:
            print("odd + not wielder")
            self.loop = self.loop*2
            self.people = range(self.people[1], self.people[-1], self.loop)
            self.wielder = True
            self.reset_odd_or_even()

        if len(self.people) == 1:
            return self.people[0]

    def return_winner(self):
        while True:
            result = self.execute()
            if result:
                return result
