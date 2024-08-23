class CircleIterator:
    def __init__(self, num):
        self.people = range(1, num + 1, 1)
        self.wielder = True
        self.even = len(self.people) % 2 == 0
        self.loop = 1

    def reset_odd_or_even(self):
        self.even = len(self.people) % 2 == 0

    def execute(self):
        self.loop = self.loop * 2
        if self.even and self.wielder:
            self.people = range(self.people[0], self.people[-1], self.loop)

        elif not self.even and self.wielder:
            self.people = range(self.people[0], self.people[-1] + 1, self.loop)
            self.wielder = False

        elif self.even and not self.wielder:
            self.people = range(self.people[1], self.people[-1] + 1, self.loop)

        elif not self.even and not self.wielder:
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
