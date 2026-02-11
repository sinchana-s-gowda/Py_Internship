class CounterIterator:
    def __init__(self):
        self.counters = {}

    def add_counter(self, name, value):
        self.counters[name] = value

    def display_counters(self):
        print(self.counters)

    def update_counter(self, name, new_value):
        if name in self.counters:
            self.counters[name] = new_value

    def delete_counter(self, name):
        if name in self.counters:
            del self.counters[name]


counter = CounterIterator()
counter.add_counter("XYZ", 1)
counter.add_counter("ABC", 2)
counter.display_counters()
counter.update_counter("XYZ", 10)
counter.delete_counter("ABC")
counter.display_counters()