class Calculator:
    def __init__(self):
        self.operations = {}

    def add_operation(self, name, result):
        self.operations[name] = result

    def display_operations(self):
        print(self.operations)

    def update_operation(self, name, new_result):
        if name in self.operations:
            self.operations[name] = new_result

    def delete_operation(self, name):
        if name in self.operations:
            del self.operations[name]


calc = Calculator()
calc.add_operation("XYZ", 10 + 20)
calc.add_operation("ABC", 30 + 40)
calc.display_operations()
calc.update_operation("XYZ", 100)
calc.delete_operation("ABC")
calc.display_operations()